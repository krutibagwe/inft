class Stu{
    private String name;
    public  Stu(){
        this.name="Unknown";
    }
    public  Stu(String name){
        this.name= name;
    }
    public String getName(){
        return name;
    }
}
public class Student{
    public static void main(String[]args){
        Stu s1= new Stu();
        Stu s2= new Stu("Alice");
        Stu s3= new Stu("Bob");
        
        System.out.println("Student 1: "+ s1.getName());
        System.out.println("Student 2: "+ s2.getName());
        System.out.println("Student 3: "+ s3.getName());
    }
}
