class PrintEven implements Runnable{
    public void run(){
        System.out.println("Even numbers are: ");
        for(int i=0; i<=10; i+=2){
            System.out.println(i);
        }
    }
}
class PrintOdd implements Runnable{
    public void run(){
        System.out.println("Odd numbers are: ");
        for(int i=1; i<=10; i+=2){
            System.out.println(i);
        }
    }
}
public class OddEven{
    public static void main(String[]args){
        Thread t1= new Thread(new PrintEven());
        Thread t2= new Thread(new PrintOdd());
        
        t1.start();
        t2.start();
    }
}
