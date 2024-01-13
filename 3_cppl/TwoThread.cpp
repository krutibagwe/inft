#include<iostream>
#include<thread>
using namespace std;

void func1(){
    cout << "Hello World!"<< endl;
}
void func2(){
    cout<< "Welcome to IT." << endl;
}
int main(){
    thread t1(func1);
    t1.join();
    thread t2(func2);
    t2.join();
    
    return 0;
}
