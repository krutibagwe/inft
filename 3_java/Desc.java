import java.util.Scanner;
public class Desc{
    public static void main(String[] args){
        Scanner scanner = new Scanner (System.in);
        System.out.println("Enter a number: ");
        int num = scanner.nextInt();
        
       while(num!=0){
           System.out.println(num);
           num--;
       }
    }
}

