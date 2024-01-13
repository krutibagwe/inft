#include <iostream>
using namespace std;

class Staff{
    public:
    void getData(){
        cout<<"Enter name: " << endl;
        cin>>name;
        cout<<"Enter code: " <<endl;
        cin>>code;
    }
    void display(){
        cout<<"Name: " << name<< endl;
        cout<< "Code: " << code << endl;
    }
    private:
    string name;
    int code;
};

class Typist: public Staff{
    public:
    void getData(){
        Staff::getData();
        cout<<"Enter speed: " << endl;
        cin>> speed;
    }
    void display(){
        Staff::display();
        cout<< "Speed: " << speed << endl;
    }
    private:
    int speed;
};

int main(){
    Typist t;
    t.getData();
    cout<<"\nDetails: "<< endl;
    t.display();
    
    return 0;
}


