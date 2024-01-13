import java.util.Scanner;
public class AreaCircle{
    public static double calcAr(double radius){
        return Math.PI * radius *radius;
    }
    
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the radius of circle: ");
        double radius= scanner.nextDouble();
        double areacircle = calcAr(radius);
        System.out.println("Area of circle is " + areacircle);
    }
}
