import java.util.*;
import java.util.regex.*;
class pattern-syntax-checker{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while(testCases>0)
        {
            String pattern = in.nextLine();
            testCases--;

            try
            {
                Pattern.compile(pattern);
                System.out.println("Valid");
            }
            catch(PatternSyntaxException ex)
            {
                System.out.println("Invalid");
            }
        }
    }
}
