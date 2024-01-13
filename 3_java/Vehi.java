interface Vehicle{
    void start();
    void stop();
}
class Bicycle implements Vehicle{
    public void start(){
        System.out.println("Bicycle is started.");
    }
    public void stop(){
        System.out.println("Bicycle is stopped.");
    }
}
class Bike implements Vehicle{
    public void start(){
        System.out.println("Bike is started.");
    }
    public void stop(){
        System.out.println("Bike is stopped.");
    }
}
class Car implements Vehicle{
    public void start(){
        System.out.println("Car is started.");
    }
    public void stop(){
        System.out.println("Car is stopped.");
    }
}

public class Vehi{
    public static void main(String[]args){
        Bicycle bc = new Bicycle();
        Bike bk = new Bike();
        Car c1= new Car();
        bc.start();
        bc.stop();
        System.out.println(" ");
        bk.start();
        bk.stop();
        System.out.println(" ");
        c1.start();
        c1.stop();
    }
}
