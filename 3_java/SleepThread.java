public class SleepThread{
    public static void main(String[]args){
        System.out.println("The thread is going to sleep for 500 ms.");
        try{
            Thread.sleep(500);
        }
        catch (InterruptedException e){
            e.printStackTrace();
        }
        System.out.println("The thread woke up after sleeping");
    }
}

