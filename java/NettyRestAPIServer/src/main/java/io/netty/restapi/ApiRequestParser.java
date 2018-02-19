package io.netty.restapi;

import com.google.gson.JsonObject;
import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.*;
import io.netty.handler.codec.http.*;
import io.netty.handler.codec.http.multipart.*;
import io.netty.handler.codec.http.multipart.Attribute;
import io.netty.util.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;


/**
 * Created by SunMyeong Lee on 2016-08-30.
 */
public class ApiRequestParser extends SimpleChannelInboundHandler<FullHttpMessage> {
    private static final Logger logger = LogManager.getLogger(ApiRequestParser.class);

    private HttpRequest request;
    private JsonObject apiResult;

    private static final HttpDataFactory factory = new DefaultHttpDataFactory(DefaultHttpDataFactory.MINSIZE);

    private HttpPostRequestDecoder decoder;

    private Map<String, String> reqData = new HashMap<>();

    private static final Set<String> usingHeader = new HashSet<>();
    static {
        usingHeader.add("token");
        usingHeader.add("email");
    }
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, FullHttpMessage msg) throws Exception {
        // Request header 처리
        if (msg instanceof HttpRequest) {
            this.request = (HttpRequest) msg;

            if (HttpHeaders.is100ContinueExpected(request)) {
                send100Continue(ctx);
            }

            HttpHeaders headers = request.headers();
            if(!headers.isEmpty()) {
                for (Map.Entry<String, String> h : headers) {
                    String key = h.getKey();
                    if (usingHeader.contains(key)) {
                        reqData.put(key, h.getValue());
                    }
                }
            }

            reqData.put("REQUEST_URI", request.getUri());
            reqData.put("REQUEST_METHOD", request.getMethod().name());
        }

        if (msg instanceof HttpContent) {
            HttpContent httpContent = (HttpContent) msg;

            ByteBuf content = httpContent.content();

            if (msg instanceof LastHttpContent) {
                logger.debug("LastHttpContent message received!!" + request.getUri());

                LastHttpContent trailer = (LastHttpContent) msg;

                readPostData();

                ApiRequest service = ServiceDispatcher.dispatch(reqData);

                try {
                    service.executeService();

                    apiResult = service.getApiResult();
                }
                finally {
                    reqData.clear();
                }

                if (!writeResponse(trailer, ctx)) {
                    ctx.writeAndFlush(Unpooled.EMPTY_BUFFER)
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

    private void send100Continue(ChannelHandlerContext ctx) {

    }

    private void readPostData() {
        try {
            decoder = new HttpPostRequestDecoder(factory, request);
            for (InterfaceHttpData data : decoder.getBodyHttpDatas()) {
                if (InterfaceHttpData.HttpDataType.Attribute == data.getHttpDataType()) {
                    try {
                        Attribute attribute = (Attribute) data;
                        reqData.put(attribute.getName(), attribute.getValue());
                    } catch (IOException e) {
                        logger.error("BODY Attribute: " + data.getHttpDataType().name(), e);
                        e.printStackTrace();
                    }
                } else {
                    logger.info("BODY data : " + data.getHttpDataType().name() + ": " + data);
                }
            }
        } catch (HttpPostRequestDecoder.ErrorDataDecoderException e) {
            logger.error(e);
        }
        finally {
            if (decoder != null) {
                decoder.destroy();
            }
        }
    }
}
