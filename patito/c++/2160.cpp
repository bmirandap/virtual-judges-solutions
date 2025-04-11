// Problem ID: 2160
// Title: Numeros en ingles

#include <iostream>

using namespace std;

int main()
{
    short n;
    cin  >> n;
    switch(n){
        case 2: cout << "two"; break;
        case 3: cout << "three"; break;
        case 5: cout << "five"; break;
        case 7: cout << "seven"; break;
        default: cout << "numero no valido"; break;
    }
    
    return 0;
}