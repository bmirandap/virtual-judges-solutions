// Problem ID: 1031
// Title: Mediana

import java.util.Arrays;
import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    int n;
	    Scanner sc = new Scanner(System.in);
	    while(sc.hasNext()){
	        n = sc.nextInt();
	        int num[] = new int[n];
	        for(int i = 0; i <n; i++){
	            num[i] = sc.nextInt();
	        }
	        Arrays.sort(num);
	        if( n % 2 == 0 ){
	            System.out.println("-1");
	        }else{
	            int pos = (int)(n/2);
	            if( pos == 0 ){
	                System.out.println(num[pos]);
	            }else{
	                if(num[pos] != num[pos-1] && num[pos] != num[pos+1]){
	                    System.out.println(num[pos]);
	                }else{
	                    System.out.println("-1");
	                }
	            }
	        }
	    }
	}
}