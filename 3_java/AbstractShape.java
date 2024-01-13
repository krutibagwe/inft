abstract class Shape{
    abstract void draw();
}
class Rectangle extends Shape{
    void draw(){
        System.out.println("Drawing a rectangle.");
    }
}
class Circle extends Shape{
    void draw(){
        System.out.println("Drawing a circle.");
    }
}

public class AbstractShape{
    public static void main(String[]args){
        Rectangle r1= new Rectangle();
        Circle c1= new Circle();
        r1.draw();
        c1.draw();
    }
}
