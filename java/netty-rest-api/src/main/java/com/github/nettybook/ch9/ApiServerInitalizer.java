package com.github.nettybook.ch9;

import com.github.nettybook.ch9.core.ApiRequestParser;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.http.HttpContentCompressor;
import io.netty.handler.codec.http.HttpObjectAggregator;
import io.netty.handler.codec.http.HttpRequestDecoder;
import io.netty.handler.codec.http.HttpResponseEncoder;
import io.netty.handler.ssl.SslContext;


/**
 * Created by SunMyeong Lee on 2018-08-07.
 */
public class ApiServerInitalizer extends ChannelInitializer<SocketChannel> {

    private final SslContext sslContext;

    public ApiServerInitalizer(SslContext sslContext) {
        this.sslContext = sslContext;
    }

    protected void initChannel(SocketChannel socketChannel) throws Exception {
        ChannelPipeline p = socketChannel.pipeline();
        if (sslContext != null)
            p.addLast(sslContext.newHandler(socketChannel.alloc()));

        p.addLast(new HttpRequestDecoder());
        p.addLast(new HttpObjectAggregator(65536));
        p.addLast(new HttpResponseEncoder());
        p.addLast(new HttpContentCompressor());
        p.addLast(new ApiRequestParser());
    }
}
