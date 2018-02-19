import Foundation
import UIKit


struct PCXhead {
    var identity: u_char?
    var pcxver: u_char?
    var compression: u_char?
    var bpp: u_char?
    var x1: u_short?
    var y1: u_short?
    var x2: u_short?
    var y2: u_short?
    var HRes: u_short?
    var VRes: u_short?
    var colormap: NSData? // 16 * 3
    var Reserved1: u_char?
    var Numplanes: u_char?
    var BPL: u_short?
    var pallinfo: u_short?
    var width: u_short?
    var height: u_short?
    var filler: NSData?  // 54
}
public struct PixelData {
    var a: UInt8 = 255
    var r: UInt8
    var g: UInt8
    var b: UInt8
}

private let rgbColorSpace = CGColorSpaceCreateDeviceRGB()
private let bitmapInfo:CGBitmapInfo = CGBitmapInfo(rawValue: CGImageAlphaInfo.PremultipliedFirst.rawValue)
public func imageFromARGB32Bitmap(pixels:[PixelData], width: Int, height: Int) -> UIImage {
    let bitsPerComponent: Int = 8
    let bitsPerPixel: Int = 32
    
    assert(pixels.count == Int(width * height))
    
    var data = pixels
    
    let providerRef = CGDataProviderCreateWithCFData(NSData(bytes: &data, length: data.count * sizeof(PixelData)))
    
    let cgim = CGImageCreate(
        width,
        height,
        bitsPerComponent,
        bitsPerPixel,
        width * sizeof(PixelData),
        rgbColorSpace,
        bitmapInfo,
        providerRef,
        nil,
        true,
        .RenderingIntentDefault
    )
    
    return UIImage(CGImage: cgim!)
}

func pcxDataToImage(rawData: NSData) -> UIImage {
    var data = BinaryDataScanner(data: rawData, littleEndian: true, encoding: NSUTF8StringEncoding)
    var bmpData = [UInt8]()
    var colors = [PixelData]()
    var pixels = [PixelData]()
    
    let pcxHead = PCXhead(
        identity : data.readByte(),
        pcxver : data.readByte(),
        compression : data.readByte(),
        bpp : data.readByte(),
        x1 : data.read16(),
        y1 : data.read16(),
        x2 : data.read16(),
        y2 : data.read16(),
        HRes : data.read16(),
        VRes : data.read16(),
        colormap : data.readDataForSize(16*3),
        Reserved1 : data.readByte(),
        Numplanes : data.readByte(),
        BPL : data.read16(),
        pallinfo : data.read16(),
        width : data.read16(),
        height : data.read16(),
        filler : data.readDataForSize(54)
    )
    let iScanLineSize = Int(pcxHead.BPL!) * Int(pcxHead.Numplanes!)
    
    let xInit = Int(pcxHead.x1!)
    let yInit = Int(pcxHead.y1!)
    let width = Int(pcxHead.x2!) - Int(pcxHead.x1!) + 1
    let height = Int(pcxHead.y2!) - Int(pcxHead.y1!) + 1
    var tx = xInit
    var ty = yInit
    
    var c: UInt8  // for data.readByte()
    var runlen: Int // for run-length encoding
    var drawing = true
    
    while (drawing) {
        c = data.readByte()!
        
        /* check for run */
        if((c & 0xc0) == 0xc0) {
            runlen = Int(c & 0x3f)
            
            c = data.readByte()!
        }
        else {
            runlen = 1
        }
        
        
        
        repeat {
            if ( tx < width ) {
                bmpData.append(c)
            }
            
            tx += 1
            runlen -= 1
            
            
            if ( tx >= iScanLineSize ) {
                tx = xInit
                ty += 1
                runlen = 0
            }
            if ( ty >= height ) {
                drawing = false
            }
            
            
        } while( drawing && runlen > 0 )
    }
    
    
    /* Setting Palette */
    if ( data.readByte() == 12 ) {
        for _ in 0 ..< 256 {
            let a = UInt8(255)
            let r = data.readByte()!
            let g = data.readByte()!
            let b = data.readByte()!
            
            colors.append(PixelData(a: a, r: r, g: g, b: b))
        }
    }
    
    for i in bmpData {
        pixels.append(colors[Int(i)])
    }
    
    return imageFromARGB32Bitmap(pixels, width: width, height: height)
}

