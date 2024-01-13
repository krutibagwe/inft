class Table{
synchronized void printTable(int n){
    for(int i=1; i<=5; i++){
        System.out.println(n*i);
    try{
        Thread.sleep(400);
    }
    catch (Exception e){
        System.out.println( e.getMessage());
    }
    }
}
}

class myThread1 extends Thread{
    Table t;
    myThread1(Table t1){
        this.t = t1;
    }
    public void run(){
        t.printTable(3);
       
    }
}

class myThread2 extends Thread{
    Table t;
    myThread2(Table t1){
        this.t = t1;
    }
    public void run(){
        t.printTable(11);
       
    }
}

class SynchroTable{
public static void main(String [] args){
        Table T1= new Table();
        myThread1 th1= new myThread1(T1);
        th1.start();
        myThread2 th2= new myThread2(T1);
        th2.start();
    }
}
