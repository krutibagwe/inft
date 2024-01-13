import java.util.Scanner;
class ValidateException extends Exception{
    public ValidateException(String message){
        super(message);
    }
}
public class ValidateUser{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter username and password: ");
        String username= scanner.nextLine();
        String password= scanner.nextLine();
        
        try{
            if(username.length()<5 || password.length()<8){
                throw new ValidateException("Invalid username or password!");
            }
            System.out.println("Validation Successful.");
        } catch(ValidateException e){
            System.out.println("Error: "+ e.getMessage());
        }
    }
}
