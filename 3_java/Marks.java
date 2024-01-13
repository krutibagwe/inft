import java.util.Scanner;
class MarksOutOfBoundException extends Exception{
    public MarksOutOfBoundException(String message){
        super(message);
    }
}
public class Marks{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter the marks: ");
        int marks= scanner.nextInt();
        
        try{
            if(marks<0 || marks>100){
                throw new MarksOutOfBoundException("Marks should be between 0 and 100");
            }
            System.out.println("Marks entered are valid.");
        } catch(MarksOutOfBoundException e){
            System.out.println("Error: "+ e.getMessage());
        }
    }
}
