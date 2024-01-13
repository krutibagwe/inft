class Single extends Thread{
    public void run(){
        System.out.println("Hello World!");
    }
}
public class SingleThread{
    public static void main(String[]args){
        Single t1= new Single();
        Single t2= new Single();
        t1.start();
        t2.start();
    }
}
