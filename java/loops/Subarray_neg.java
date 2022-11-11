import java.io.*;
import java.util.*;

public class Subarray_neg {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int negCnt = 0;
        for (int i=0; i < n; i++) {
            arr[i] = sc.nextInt(); 
            int j = i;
            int sum = 0;
            while (j>=0) {
                sum += arr[j];
                if(sum < 0)
                    negCnt++;
                j--;
            }
         }        
        System.out.println(negCnt); 
    }
}
