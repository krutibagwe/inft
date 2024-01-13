import java.util.Scanner;
public class Largest3{
    public static void main(String[] args){
        Scanner scanner = new Scanner (System.in);
        System.out.println("Enter three numbers: ");
        int n1 = scanner.nextInt();
        int n2 = scanner.nextInt();
        int n3 = scanner.nextInt();
        
        
        if(n1>=n2 && n1>=n3){
            System.out.println(n1 + " is the largest number.");
        }
        else if (n2>=n1 && n2>=n3){
            System.out.println(n2 + " is the largest number.");
        }
        else{
            System.out.println(n3 + " is the largest number.");
        }
    }
}
