// Problem ID: 2284
// Title: Reto1
// Last modification: 09-May-2022
#include <iostream>

using namespace std;

int mayor(int x, int y){
    return x > y ? x : y;
}

int main()
{
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;
    
    cout << mayor(a, mayor(b, c));
    
    return 0;
}