import java.util.*;

class Java_String_Tokens{
	public static void main(String[] args) {
	    Scanner scan = new Scanner(System.in);
	    String s = scan.nextLine();
	    // Write your code here.
	    if(s.trim().length()==0){
	        System.out.println("0");
	    }
	    else{
	        String[] strArry = s.trim().split("[ !,?._'@]+");
	        System.out.println(strArry.length);
	        for(String c:strArry){
	        System.out.println(c);
	        }
	    }
	}
}
