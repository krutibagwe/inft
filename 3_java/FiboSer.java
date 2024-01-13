import java.util.Scanner;
public class FiboSer{
    static void FiboSer(int n){
        int a=0, b=1;
        for(int i=0; i<n; i++){
            System.out.println(a + " ");
            int nxt= a+b;
            a=b;
            b=nxt;
            
        }
    }
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the number: ");
        int n = scanner.nextInt();
        System.out.println("Fibonacci Series: ");
        FiboSer(n);
    }
}

