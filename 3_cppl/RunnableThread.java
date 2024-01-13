class Th implements Runnable{
    public void run(){
        System.out.println("Hello World!");
    }
}
public class RunnableThread{
    public static void main(String[]args){
        Th t1= new Th();
        Thread t= new Thread(t1);
        t.start();
    }
}
