import java.math.BigDecimal; 
import java.util.*;
public class Decimal_sort {
	    public static void main(String []args) {
	        Scanner scan = new Scanner(System.in);
	        int n = scan.nextInt();         
	        String [] s = new String [n];
	        for(int i=0; i<n; i++)
	        {
	            s[i] = scan.next();    
	        }
	        System.out.println();
	        Arrays.sort(s, 0, n, (a, b) -> new BigDecimal(b).compareTo(new BigDecimal(a)));
	        for(int i=0; i<n; i++)
	        	{
	            System.out.println(s[i]);    //prints out the new string in order
	        	}
	    }
	}
