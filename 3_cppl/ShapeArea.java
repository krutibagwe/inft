abstract class Shape{
    abstract double areaRect(double length, double breadth);
    abstract double areaSquare(double side);
    abstract double areaCircle(double radius);
}

class Area extends Shape{
    double areaRect(double length, double breadth){
        return length* breadth;
    }
    double areaSquare(double side){
        return side* side;
    }
    double areaCircle(double radius){
        return Math.PI * radius* radius;
    }
}

public class Main{
    public static void main(String[]args){
        Area a= new Area();
        System.out.println("Area of rectangle: "+ a.areaRect(5,4));
        System.out.println("Area of square: "+ a.areaSquare(6));
        System.out.println("Area of circle: "+ a.areaCircle(3));
    }
}
