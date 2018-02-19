package io.netty.restapi;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

/**
 * Created by SunMyeong Lee on 2016-08-30.
 */
public class ApiServerMain {
    public static void main(String[] args) {
        AbstractApplicationContext springContext = null;
        try {
            springContext = new AnnotationConfigApplicationContext(ApiServerConfig.class);
            springContext.registerShutdownHook();

            ApiServer server = springContext.getBean(ApiServer.class);
            server.start();
        }
        finally {
            springContext.close();
        }
    }
}
