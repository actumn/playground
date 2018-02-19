import org.apache.log4j.LogManager;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by SunMyeong Lee on 2016-07-03.
 */
public class Log4jParseTest {

    public static void main(String[] args) {
        String[] samples = {
                "2016-07-03 21:07:07 INFO Log4jTest - information"
        };

        String regex = "(\\d{4}-\\d{2}-\\d{2}) (\\d{2}:\\d{2}:\\d{2}) ([^ ]*) ([^ ]*) - (.*)$";

        Pattern p = Pattern.compile(regex);

        Matcher m = p.matcher(samples[0]);

        if (m.matches() && m.groupCount() == 5) {
            String date = m.group(1);
            String time = m.group(2);
            String priority = m.group(3);
            String category = m.group(4);
            String message = m.group(5);

            System.out.println("date: " + date);
            System.out.println("time: " + time);
            System.out.println("priority: " + priority);
            System.out.println("category: " + category);
            System.out.println("message: " + message);
        }
    }
}
