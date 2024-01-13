public class NestedTryCatch{
    public static void main(String[]args){
        try{
            int a[]= {1,2,3,4,5};
            System.out.println(a[6]);
            
            try{
                int div = 5/0;
            } catch(ArithmeticException e2){
                System.out.println("Error:" + e2.getMessage());
            }
        }catch (ArrayIndexOutOfBoundsException e1){
            System.out.println("error: "+ e1.getMessage());
        }
    }
}
