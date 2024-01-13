import java.util.Scanner;
public class ArrRev{
    public static void main(String[]args){
        Scanner scanner=new Scanner(System.in);
        System.out.println("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] arr= new  int[n];
        System.out.println("Enter the elements of the array: ");
        
        for (int i=0; i<n; i++){
            arr[i]= scanner.nextInt();
        }
        
        for(int i =0; i<n/2; i++){
            int temp = arr[i];
            arr[i]= arr[n-1-i];
            arr[n-1-i]= temp;
        }
        
        System.out.println("The array in reversed order is: ");
        for (int i=0; i<n; i++){
            System.out.println(arr[i]);
        }
    }
}
