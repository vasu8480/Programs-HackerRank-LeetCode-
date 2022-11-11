import java.io.*;
import java.util.*;

public class primitive_data {

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t=sc.nextInt();
    for(int i=0;i<t;i++)
    {
        try
        {
            long x=sc.nextLong();
            System.out.println(x+" can be fitted in:");
            if(x == (byte)x)System.out.println("* byte");
            if(x == (short)x)System.out.println("* short");
            if(x == (int)x)System.out.println("* int");
            if(x == (long)x)System.out.println("* long");
        }
        catch(Exception e)
        {
            System.out.println(sc.next()+" can't be fitted anywhere.");
        }

    }
}
}
