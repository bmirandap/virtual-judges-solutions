// Problem ID: 1245
// Title: De arriba hacia abajo

import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int x, y, may, men;
	    x = sc.nextInt();
	    y = sc.nextInt();
	    if( x > y ){
	        may = x;
	        men = y;
	    }else{
	        may = y;
	        men = x;
	    }
	    while(may >= men){
	        System.out.println(may);
	        may -= 1;
	    }
	}
}