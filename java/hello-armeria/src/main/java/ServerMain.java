import com.linecorp.armeria.common.HttpResponse;
import com.linecorp.armeria.common.HttpStatus;
import com.linecorp.armeria.common.MediaType;
import com.linecorp.armeria.server.Server;
import com.linecorp.armeria.server.ServerBuilder;

import java.util.concurrent.CompletableFuture;

public class ServerMain {
    public static void main(String[] args) {
        ServerBuilder builder = new ServerBuilder();
        builder.http(8080);

        builder.annotatedService(new CustomService());

        Server server = builder.build();
        CompletableFuture<Void> future = server.start();
        future.join();
    }
}
