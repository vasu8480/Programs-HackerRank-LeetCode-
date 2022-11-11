import java.math.*; 
import java.util.*;
public class 1d-array {
    public static void main(String []args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();         
        String [] s = new String [n];
        for(int i=0; i<n; i++)
        {
            s[i] = scan.next();    
        }
        for(String j:s)
        {
            System.out.println(j);
      
          }
    } 
}
    
