class Th1 extends Thread{
    public void run(){
        System.out.println("Welcome! ");
    }
}
class Th2 extends Thread{
    public void run(){
        System.out.println("Welcome to IT!");
    }
}
public class TwoThread{
    public static void main(String[]args){
        Th1 t1= new Th1();
        Th2 t2= new Th2();
        t1.start();
        t2.start();
    }
}
