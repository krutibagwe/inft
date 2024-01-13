public class Car{
    private String brand;
    private int year;
    
    public Car(){
        this("Unknown", 0);
    }
    public Car(String brand, int year){
        this.brand = brand;
        this.year=year;
    }
    public String getBrand(){
        return brand;
    }
    public int getYear(){
        return year;
    }
    
    public static void main(String[]args){
        Car c1= new Car();
        Car c2= new Car("Toyota", 2013);
        
       System.out.println("Brand of car 1: "+ c1.getBrand()+ " year: "+ c1.getYear());
       System.out.println("Brand of car 2: "+ c2.getBrand()+ " year: "+ c2.getYear());
    }
}
