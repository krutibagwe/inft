#include<iostream>
#include<string>
using namespace std;

class String{
    public:
    void setString(string s){
        str=s;
    }
    protected:
    string str;
};

class ReverseString : public String{
    public:
    void reverse(){
        int n= str.length();
        for(int i=0; i<n/2; i++){
            swap(str[i], str[n-i-1]);
        }
    }
    void display(){
        cout<< str<< endl;
    }
};

int main(){
    ReverseString rs;
    rs.setString("Hello World");
    rs.reverse();
    rs.display();
}
