import java.util.Scanner;
public class Fibonacci{
     public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the number: ");
        int n = scanner.nextInt();
        System.out.println("Fibonacci Series: ");
        int a=0, b=1;
        for(int i=0; i<n; i++){
            System.out.print(a + " ");
            int nxt= a+b;
            a=b;
            b=nxt;
            
        }
    }
}
