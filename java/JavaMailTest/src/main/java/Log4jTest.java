import org.apache.log4j.Logger;

/**
 * Created by SunMyeong Lee on 2016-07-03.
 */
public class Log4jTest {
    private final Logger logger = Logger.getLogger(Log4jTest.class);

    public void logTest(String msg) {
        try {
            logger.info(msg);
        } catch (Exception e) {
            logger.error("get error", e);
        }
    }

    public static void main(String[] args) {
        Log4jTest obj = new Log4jTest();
        obj.logTest("information");
    }
}
