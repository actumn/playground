public class BasicSynchronization {
    private String message;

    public static void main(String[] args) {
        BasicSynchronization temp = new BasicSynchronization();

        System.out.println("Test starts");
        new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                temp.callMe("Thread1");
            }
        }).start();
        new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                temp.callMe("Thread2");
            }
        }).start();
        System.out.println("Test ends");
    }

    public synchronized void callMe(String whoCallMe) {
        message = whoCallMe;

        try {
            long sleep = (long) (Math.random() * 100);
            Thread.sleep(sleep);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println(whoCallMe);
        if (!message.equals(whoCallMe)) {
            System.out.println(whoCallMe + " | " + message);
        }
    }
}
