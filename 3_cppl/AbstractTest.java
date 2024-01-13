abstract class Animal{
    abstract void animalType();
    void action(){
        System.out.println("Eating");
    }
}
class Dog extends Animal{
    void sound(){
        System.out.println("Barking");
    }
    void animalType(){
        System.out.println("I am a dog.");
    }
}
public class AbstractTest{
    public static void main(String[]args){
        Dog d1= new Dog();
        d1.action();
        d1.sound();
        d1.animalType();
    }
}

