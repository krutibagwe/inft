import java.util.Scanner;
public class Duplicate{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the size of array: ");
        int size= scanner.nextInt();
        
        System.out.println("Enter the elements of array: ");
        int[] num= new int [size];
        for(int i=0; i<size; i++){
            num[i]=scanner.nextInt();
        }
        
        boolean hasDuplicates=false;
        for(int i=0; i<num.length-1; i++){
            for(int j=i+1; j<num.length; j++){
                if(num[i]==num[j]){
                    hasDuplicates=true;
                    break;
                }
            }
            if(hasDuplicates){
                break;
            }
        }
        if(hasDuplicates){
            System.out.println("There are duplicate elements in the array.");
        }
        else{
            System.out.println("There are no duplicate elements in the array.");
        }
    }
}
