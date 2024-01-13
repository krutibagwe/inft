import java.util.Scanner;
public class Prime{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the first number: ");
        int lower= scanner.nextInt();
        System.out.println("Enter the second number: ");
        int upper= scanner.nextInt();
        System.out.println("Prime numbers between " +lower+ " and " + upper+ " are: ");
        
        for(int num=lower; num<=upper; num++){
            int count=0;
            for(int i=1; i<=num; i++){
                if(num%i==0){
                    count++;
                }
            }
            if(count==2){
            System.out.print(num + " ");
            }
       
        }
    }
}
