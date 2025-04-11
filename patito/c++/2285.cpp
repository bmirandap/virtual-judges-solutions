// Problem ID: 2285
// Title: Reto2

#include <iostream>

using namespace std;

int mayor(int x, int y){
    return x > y ? x : y;
}

int menor(int x, int y){
    return x < y ? x : y;
}

int main()
{
    int a, b, c, d;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    
    cout << mayor(a, mayor(b, mayor(c, d))) << endl;
    cout << menor(a, menor(b, menor(c, d)));
    
    return 0;
}