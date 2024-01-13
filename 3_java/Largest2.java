import java.util.Scanner;
public class Largest2{
  public static void main(String[]args){
    Scanner scanner= new Scanner(System.in);
    System.out.println("Enter two numbers: ");
    int a= scanner.nextInt();
    int b= scanner.nextInt();

    if(a>b){
      System.out.println(a + " is the largest.");
    }
    else if(b>a){
      System.out.println(b+ "  is the largest.");
    }
    else{
      System.out.println("Both numbers are equal.");
    }
  }
}
