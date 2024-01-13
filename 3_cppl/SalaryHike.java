class Employee{
    double salary=10000;
}
class PermenantEmp extends Employee{
    double hike(){
        return salary*0.35;
    }
}
class TemporaryEmp extends Employee{
    double hike(){
        return salary*0.2;
    }
}
public class SalaryHike{
    public static void main(String[]args){
        PermenantEmp p1= new PermenantEmp();
        TemporaryEmp t1 = new TemporaryEmp();
        
        System.out.println("Hike of permenant employee: "+ p1.hike());
        System.out.println("Hike of temporary employee: "+ t1.hike());
    }
}
