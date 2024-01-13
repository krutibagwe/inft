#include<iostream>
using namespace std;

class Area{
    public:
    int getArea(int l, int b){
        return l*b;
    }
};
class Perimeter{
    public:
    int getPerimeter(int l, int b){
        return 2* (l+b);
    }
};

class Rectangle: public Area, public Perimeter{
    public:
    Rectangle(int l, int b): length(l), breadth(b){}
    void display(){
        cout<< "length: "<< length<< " & breadth: "<< breadth<< endl;
        cout << "Area: " << getArea(length, breadth)<< endl;
        cout << "Perimeter: " << getPerimeter(length, breadth) << endl;
    }
    private:
    int length;
    int breadth;
};

int main(){
    Rectangle r(5,10);
    r.display();
    
    return 0;
}



