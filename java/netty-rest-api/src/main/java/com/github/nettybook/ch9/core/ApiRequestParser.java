package com.github.nettybook.ch9.core;

import com.google.gson.JsonObject;
import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.ChannelFutureListener;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.handler.codec.http.*;
import io.netty.handler.codec.http.multipart.DefaultHttpDataFactory;
import io.netty.handler.codec.http.multipart.HttpDataFactory;
import io.netty.handler.codec.http.multipart.HttpPostRequestDecoder;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import static io.netty.handler.codec.http.HttpResponseStatus.CONTINUE;
import static io.netty.handler.codec.http.HttpVersion.HTTP_1_1;

/**
 * Created by SunMyeong Lee on 2018-08-07.
 */
public class ApiRequestParser extends SimpleChannelInboundHandler<FullHttpMessage> {
    private static final Logger logger = LogManager.getLogger(ApiRequestParser.class);

    private HttpRequest request;
    private JsonObject apiResult;

    private static final HttpDataFactory factory = new DefaultHttpDataFactory(DefaultHttpDataFactory.MINSIZE);

    private HttpPostRequestDecoder decoder;

    private Map<String, String> reqData = new HashMap<String, String>();

    private static final Set<String> usingHeader = new HashSet<String>();
    static {
        usingHeader.add("token");
        usingHeader.add("email");
    }


    protected void channelRead0(ChannelHandlerContext channelHandlerContext, FullHttpMessage fullHttpMessage) throws Exception {
        // Request header
        if (fullHttpMessage instanceof HttpRequest) {
            this.request = (HttpRequest) fullHttpMessage;

            if (HttpHeaders.is100ContinueExpected(request)) {
                send100Continue()
            }

            HttpHeaders headers = request.headers();
            if (!headers.isEmpty()) {
                for (Map.Entry<String, String> h: headers) {
                    String key = h.getKey();
                    if (usingHeader.contains(key)) {
                        reqData.put(key, h.getValue());
                    }
                }
            }

            reqData.put("REQUEST_URI", request.getUri());
            reqData.put("REQUEST_METHOD", request.getMethod().name());
        }

        if (fullHttpMessage instanceof HttpContent) {
            HttpContent httpContent = (HttpContent) fullHttpMessage;

            ByteBuf content = httpContent.content();

            if (fullHttpMessage instanceof LastHttpContent) {
                logger.debug("LastHttpContent message received!!" + request.getUri());

                LastHttpContent trailer = (LastHttpContent) fullHttpMessage;

                readPostData();

                ApiRequest service = ServiceDispatcher.dispatch(reqData);

                try {
                    service.executeService();

                    apiResult = service.getApiResult();
                }
                finally {
                    reqData.clear();
                }

                if (!wriiteResponse(trailer, channelHandlerContext)) {
                    channelHandlerContext.writeAndFlush(Unpooled.EMPTY_BUFFER)
                            .addListener(ChannelFutureListener.CLOSE);
                }
                reset();
            }
        }
    }

    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) throws Exception {
        logger.info("요청 처리 완료");
        ctx.flush();
    }


    private static void send100Continue(ChannelHandlerContext ctx) {
        FullHttpResponse response = new DefaultFullHttpResponse(HTTP_1_1, CONTINUE);
        ctx.write(response);
    }

}
