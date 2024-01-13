class Person{
    private String name;
    
    public Person(String name){
        this.name=name;
    }
    public void printInfo(){
        System.out.println("Hello " + this.name);
    }
}
public class ThisKey{
    public static void main(String [] args){
        Person p1= new Person("Alice");
        Person p2= new Person("Bob");
        
        p1.printInfo();
        p2.printInfo();
    }
}
