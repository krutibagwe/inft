public class Week{
    public static void main(String[]args){
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter \n 1. for Monday \n 2. for Tuesday\n 3. for Wednesday\n");
        System.out.println("Enter your choice: ");
        int choice = scanner.nextInt();
        
        switch(choice){
            case 1:
                System.out.println("Monday");
                break;
            case 2: 
                System.out.println("Tuesday");
                break;
             case 3: 
                System.out.println("Wednesday");
                break;
            default:
            System.out.println("Wrong choice.");
        }
    }
}
