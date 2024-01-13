import java.util.Scanner;
class Rect{
    private double length;
    private double breadth;
    
    public Rect(double length, double breadth){
        this.length = length;
        this.breadth = breadth;
    }
    
    public double printAr(){
        return length * breadth;
    }
}

public class AreaRectangle{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the length and breadth: ");
        double l = scanner.nextDouble();
        double b = scanner.nextDouble();
        
        Rect rect1= new Rect(l,b);
        
        double res= rect1.printAr();
        System.out.println("Area of rectangle is: " + res);
    }
}

