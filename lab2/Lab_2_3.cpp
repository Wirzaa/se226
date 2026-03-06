#include <iostream>

using namespace std;

int main(){
    cout << "Enter an integer between(inclusive) 3 and 9: ";
    int num;
    cin >> num;

    for(int i = 0; i<num+2; i++){
        for(int j = 1; j<i; j++){
            cout << j;
        }
        cout << endl;
    }
    for(int i = num-1; i >= 0; i--){
        for(int j = 1; j < i; j++){
            cout << j;
        }
        cout << endl;
    }
    return 0;
}