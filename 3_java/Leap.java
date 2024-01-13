import java.util.Scanner;
public class Leap{
    public static void main(String[] args){
        Scanner scanner = new Scanner (System.in);
        System.out.println("Enter the year: ");
        int year = scanner.nextInt();
        
        if(year %4 ==0){
            System.out.println(year + " is a leap year.");
        }
        else{
            System.out.println(year + " is not a leap year.");
        }
    }
}
