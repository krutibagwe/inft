#include <iostream>
#include <thread>

using namespace std;

void func1() {
    cout << "Hello, World!" << endl;
  
    thread::id threadId = this_thread::get_id();
    cout << "Thread ID of the current thread: " << threadId << endl;
}

int main() {
    thread t1(func1);
    t1.join();
    
    return 0;
}
