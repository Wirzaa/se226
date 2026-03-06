#include <iostream> 

using namespace std;

int main(){
    cout << "Enter an positive integer between(inclusive) 10 and 100: ";
    int x;
    cin >> x;
    int fCount = 0;
    int bCount = 0;
    int fbCount = 0;

    while(x < 10 || x > 100){
        cout << "Enter an positive integer between(inclusive) 10 and 100: ";
        int x;
        cin >> x;
    }
    
    for(int i = 1; i < x+1; i++){
        if(i%7 == 0){
            cout << i << " is skipped." << endl;
        }
        else if(i%3 == 0 && i%5 == 0){
            cout << "FizzBuzz" << endl;
            fbCount++;
        }
        else if(i%3 == 0){
            cout << "Fizz" << endl;
            fCount++;
        }
        else if(i%5 == 0){
            cout << "Buzz" << endl;
            bCount++;
        }
        else{
            cout << i << endl;
        }
    }

    cout << "--- Summary ---" << endl;
    cout << "Fizz Count: " << fCount << endl;
    cout << "Buzz Count: " << bCount << endl;
    cout << "FizzBuzz Count: " << fbCount << endl;

    return 0;


}