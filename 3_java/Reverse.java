import java.util.Scanner;
public class Reverse{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = scanner.nextInt();
        int revnum = revnum(num);
        System.out.println("Reverse of the number "+ num + " is " + revnum);
    }
    
    public static int revnum(int num){
        int revn = 0;
        while(num !=0){
            int digit = num %10;
            revn = revn *10 + digit;
            num /=10;
        }
        return revn;
    }
}
