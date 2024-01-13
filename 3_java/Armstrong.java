import java.util.Scanner;
public class Armstrong{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the number: ");
        int num= scanner.nextInt();
        int originalNum=num;
        int count=0, sum=0;
        
        int temp= originalNum;
        while(temp!=0){
            temp/=10;
            count++;
        }
        
        temp= originalNum;
        while(temp!=0){
            int digit = temp %10;
            sum += Math.pow(digit, count);
            temp/=10;
        }
        if(sum==originalNum){
            System.out.println(originalNum+ " is an Armstrong number.");
        }
        else{
            System.out.println(originalNum+ " is not an Armstrong number.");
        }
    }
}
