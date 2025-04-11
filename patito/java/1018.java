// Problem ID: 1018
// Title: Operadores Relacionales

import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    int t, a, b;
	    Scanner sc = new Scanner(System.in);
	    t = sc.nextInt();
	    for(int i = 0; i< t; i++){
	        a = sc.nextInt();
	        b = sc.nextInt();    
	        if(a > b)
	            System.out.println(">");
	        else if(a<b)
	            System.out.println("<");
	        else
	            System.out.println("=");
	    }
	}
}