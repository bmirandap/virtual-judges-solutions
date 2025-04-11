// Problem ID: 1988
// Title: Lucas, ¿Alguna vez harás tu tarea?

import java.util.*;

public class Main {
	
    public static int MAX = 1000000;
    public static boolean primos[] = new boolean[MAX + 1];
    static int C[] = new int[10000001];
    static int N = 10000000;
    static int suma = 0;

    public static void main(String[] args){
        Scanner lee = new Scanner(System.in);
        int x;
        ini_criba();
        criba();
        int n = lee.nextInt();
        for( int i = 0; i < n; i++ ){
        	x = lee.nextInt();
            suma = 0;
            factorPrimo(x);
            if( primos[suma] ){
            	System.out.println("ES PRIMO");
            }
            else{
                System.out.println("NO ES PRIMO");
            }
		}
    }
    private static void criba(){
        for( int i = 0; i <= MAX; i++ ){
            primos[i] = true;
        }
        primos[0] = primos[1] = false;
        for( int i = 2; i <= MAX; i++ ){
            if( primos[i] ){
                for( int j = i + i; j <= MAX; j = j + i ){
                    primos[j] = false;
                }
            }
        }
    }
    public static void ini_criba(){
        for( int i = 0; i <= N; i++ ){
            C[i] = i;
        }
        C[0] = -1;
        C[1] = -1;
        for( int i = 2; i * i <= N; i++ ){
            if( C[i] == i ){
                for( int j = i + i; j <= N; j += i ){
                    C[j] = i;
                }
            }
        }
    }
    public static void factorPrimo(int X) {
        if( X <= 1 )
            return;
        int cont = 1;
        int Y = X / C[X];
        while( C[X] == C[Y] ){
            cont++;
            Y = Y / C[Y];
        }
        factorPrimo(Y);
        suma += C[X]*cont;
    }
}