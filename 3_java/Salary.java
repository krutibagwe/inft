import java.util.Scanner;
public class Salary{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the employee id: ");
        String id= scanner.nextLine();
        System.out.println("Enter the employee name: ");
        String name= scanner.nextLine();
        System.out.println("Enter the employee salary: ");
        double sal= scanner.nextDouble();
        
        double da= sal*0.7;
        double hra= sal *0.3;
        double cca= 240;
        double pf= sal *0.1;
        double pt= 100;
        
        double gross = sal + da + hra + cca;
        double net = gross - pf - pt;
        
        System.out.println("Employee ID: "+id);
        System.out.println("Employee Name: " + name);
        System.out.println("Base salary: "+ sal);
        System.out.println("Gross salary: "+ gross);
        System.out.println("Net salary: "+ net);
        
    }
}
