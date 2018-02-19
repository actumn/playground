import Foundation

let rawData = NSData(contentsOfFile: "/path/to/pcx")
var image = pcxDataToImage(rawData!)