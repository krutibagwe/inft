import java.util.Scanner;
public class Fact{
    public static void main(String[] args){
        Scanner scanner = new Scanner (System.in);
        System.out.println("Enter a number: ");
        int num = scanner.nextInt();
        long factorial = factorial(num);
        System.out.println("Factorial of " + num + "is " + factorial);
    }
    public static long factorial(int num){
        long result =1;
        for (int i=1; i<=num; i++){
             result *=i;
        }
        return result;
    }
}
