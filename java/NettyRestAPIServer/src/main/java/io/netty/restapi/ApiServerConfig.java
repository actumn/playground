package io.netty.restapi;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.*;
import org.springframework.context.support.PropertySourcesPlaceholderConfigurer;

import java.net.InetSocketAddress;

/**
 * Created by SunMyeong Lee on 2016-08-30.
 */
@Configuration
@ImportResource("classpath:spring/hsqlApplicationContext.xml")
@ComponentScan("com.github.nettybook.ch9, com.github.nettybook.ch9.service")
@PropertySource("classpath:api-server.properties")
public class ApiServerConfig {
    @Value("${boss.thread.count}")
    private int bossThreadCount;

    @Value("${worker.thread.count}")
    private int workerThreadCount;

    @Value("${tcp.port}")
    private int tcpPort;

    @Bean(name = "bossThreadCount")
    public int getBossThreadCount() {
        return bossThreadCount;
    }

    @Bean(name = "workerThreadCount")
    public int getWorkerThreadCount() {
        return workerThreadCount;
    }

    public int getTcpPort() {
        return tcpPort;
    }

    @Bean(name = "tcpSocketAddress")
    public InetSocketAddress tcpPort() {
        return new InetSocketAddress(tcpPort);
    }

    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
}
