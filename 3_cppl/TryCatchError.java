class TryCatchError{
    public static void main(String[]args){
        try{
            try{
                int a[]= new int[5];
                System.out.println(a[6]);
            } catch (ArrayIndexOutOfBoundsException e){
                System.out.println("Inner Catch: Array Index Out Of Bound => "+ e.getMessage());
            }
            int num= 5/0;
            System.out.println(num);
        } catch (ArithmeticException e){
            System.out.println("Outer Catch: Arithmetic Exception => "+ e.getMessage());
        }
    }
}
