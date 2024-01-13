class Animal{
    void sound(){
        System.out.println("Dog makes a sound");
    }
}
class Dog extends Animal{
    void sound(){
    super.sound();
        System.out.println("Dog barks!");
    }
}
public class Sup{
    public static void main(String[]args){
        Dog d1= new Dog();
        d1.sound();
    }
}
