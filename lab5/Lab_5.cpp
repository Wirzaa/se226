#include <iostream>

using namespace std;

int pow(int x, int y){
    int fVal = 1;
    for(int i = 0; i < y;i++){
        fVal *= x;
    }
    return fVal;
}

int my_func(int n, int r){
    if(n >= 0){
        return (pow(r, n) + my_func(n-1,r));
    }
    else{
        return 0;
    }    
}

int main(){
    int nVal;
    int rVal;
    cout << "Enter your n value: ";
    cin >> nVal;
    cout << "ENter your r value: ";
    cin >> rVal;

    cout << my_func(nVal, rVal);
}