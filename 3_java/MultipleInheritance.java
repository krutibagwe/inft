interface Parent1{
    void method1();
}
interface Parent2{
    void method2();
}
class Child implements Parent1, Parent2{
    public void method1(){
        System.out.println("Method 1 from Parent 1.");
    }
    public void method2(){
        System.out.println("Method 2 from Parent 2.");
    }
}
public class MultipleInheritance{
    public static void main(String[]args){
        Child c1= new Child();
        c1.method1();
        c1.method2();
    }
}
