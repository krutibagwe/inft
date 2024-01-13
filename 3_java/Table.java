class Table implements Runnable{
    private int num;
    
    public Table(int num){
        this.num=num;
    }
    
    public void run(){
        System.out.println("Table of " + num + ":");
        for(int i=1; i<=10; i++){
            System.out.println(num*i);
        }
    }
}

public class ThTab{
    public static void main(String[]args){
        Thread t5= new Thread(new Table(5));
        Thread t7= new Thread(new Table(7));
        Thread t13= new Thread(new Table(13));
        
        t5.start();
        t7.start();
        t13.start();
    }
}
