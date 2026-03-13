#include <iostream>

using namespace std;

int* createArray(int size);
void printArray(int* arr, int size);
void findMax(int* arr, int Size);
void swapValues(int* p1, int* p2);
void reverseArray(int* arr, int size);
void deleteArray(int* arr);

int main(){



    cout << "Creating dynamic array..." << endl << endl;

    cout << "Enter array size: ";
    int aSize;
    cin >> aSize;
    while(aSize < 1){
        cout << "Enter a proper size parameter" << endl;
    }
    int* pMyArr;
    pMyArr = createArray(aSize);
    

    cout << endl << "Enter values: ";
    for(int i = 0; i < aSize; i++){
        cin >> pMyArr[i];
        cout << " ";
    }
    cout << endl << endl;

    cout << "Array elements: " << endl;
    printArray(pMyArr, aSize);

    cout << endl << "Maximum element: ";
    findMax(pMyArr, aSize);



    cout << "-----------------" << endl;


    int A = 5;
    int B = 8;
    int* pA = &A;
    int* pB = &B;

    cout << "Swapping two numbers" << endl << endl;

    cout << "Before swap: " << endl << "a = " << *pA << endl << "b = " << *pB << endl << endl;
    swapValues(pA , pB);
    cout << "After swap: " << endl << "a = " << *pA << endl << "b = " << *pB << endl;



    cout << "-----------------" << endl;



    cout << "Reversing array..." << endl;

    reverseArray(pMyArr , aSize);

    cout << "-----------------" << endl;


    deleteArray(pMyArr);
    
    return 0;


}

int* createArray(int size){
    int* myArr = new int[size];
    return myArr;
}

void printArray(int* arr,int size){
    int* pNot = &arr[0];
    for(int i = 0; i < size; i++){
        cout <<*(pNot + i) << " ";
    }
    cout << endl;
}

void findMax(int* arr, int size){
    
    
    int maxVal = arr[0];
    for(int i = 1; i < size; i++){
        if(arr[i] > maxVal){
            maxVal = arr[i];
        }
    }
    cout << maxVal << endl;
}




void swapValues(int* p1, int* p2){
    

    

    int temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;;

    

    
}
void reverseArray(int* arr, int size){
    if(size == 1) return;

    int temp;
    
    cout << endl << "Array after reversing: " << endl;

    for(int i = 0; i < size/2; i++){
        int* p1 = arr + i;
        int* p2 = arr + size - 1 - i;
        if(*p1 == *p2) break;
        

        swapValues(p1 ,p2);
    }
    printArray(arr, size);
    
}

void deleteArray(int* arr){
    cout << "Deleting array..." << endl;
    delete[] arr;
    cout << "Memory released successfully." << endl;
}

