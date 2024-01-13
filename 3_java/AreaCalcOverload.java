import java.util.Scanner;
public class AreaCalcOverload{
    static double area(double radius){
        return Math.PI * radius * radius;
    }
    static double area(double length, double breadth){
        return length*breadth;
    }
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the radius of the circle: ");
        double r = scanner.nextDouble();
        System.out.println("Area of circle of radius "+ r +" is " + area(r));
        System.out.println("Enter the length and breadth of the rectangle: ");
        double l = scanner.nextDouble();
        double b = scanner.nextDouble();
        System.out.println("Area of rectangle of length "+ l + " and breadth " +b+ "  is " + area(l,b));
        
    }
}
