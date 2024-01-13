import java.util.Scanner;
class UserValiException extends Exception{
    UserValiException(String message){
        super(message);
    }
}
class UserValidator{
    void validateUser(String username, String password) throws UserValiException{
        if(username.length()<5 || password.length()<8){
            throw new UserValiException("Username must be greater than 5 characters and password must be greater than 8 characters");
        }
        
    }
}
public class Validate{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter usernamne and password: ");
        String username= scanner.nextLine();
        String password= scanner.nextLine();
        
        UserValidator v1= new UserValidator();
        
        try{
            v1.validateUser(username,password);
            System.out.println("Validation successful!");
        } catch(UserValiException e){
            System.out.println("Error: "+ e.getMessage());
        }
    }
}
