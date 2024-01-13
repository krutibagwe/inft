public class EncapTest{
    String name;
    int age,id;
    
    void setName(String xname){
        name= xname;
    }
    String getName(){
        return name;
    }
    void setAge(int xage){
        age= xage;
    }
    int getAge(){
        return age;
    }
    void setId(int xid){
        id= xid;
    }
    int getId(){
        return id;
    }
    
    public static void main(String[]args){
        EncapTest e1= new EncapTest();
        e1.setName("XYZ");
        System.out.println("Name: "+ e1.getName());
        e1.setAge(19);
        System.out.println("Age: "+ e1.getAge());
        e1.setId(1001);
        System.out.println("ID: "+ e1.getId());
        System.out.println(" ");
        
        EncapTest e2= new EncapTest();
        e2.setName("ABC");
        System.out.println("Name: "+ e2.getName());
        e2.setAge(23);
        System.out.println("Age: "+ e2.getAge());
        e2.setId(1002);
        System.out.println("ID: "+ e2.getId());
    }
}



