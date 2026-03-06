#include <iostream>

using namespace std;

int main(){

    int x;
    int temp;
    int steps = 0;

    cout << "Enter an integer greater than 9: ";
    cin >> x;
    temp = x;
    while(temp > 9){
        cout << x << " -->";
        temp = x%10 + (x/10)%10 + (x/100)%10;
        steps ++;
        x = temp;
    }
    cout << x << endl;
    cout << "Final value: " << x << endl;
    cout << "Total steps: " << steps;
    return 0;

}