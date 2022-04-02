import java.util.*;


class string_capitalize {
	 public static void main(String[] args) {
		 System.out.println("enter");
		 Scanner sc=new Scanner(System.in);
		 String A=sc.next();
		 String B=sc.next();
		 System.out.println(A.length()+B.length());
		 System.out.println(A.compareTo(B)>0?"Yes":"No");
		 System.out.println(A.substring(0, 1).toUpperCase()+A.substring(1)+" "+B.substring(0, 1).toUpperCase()+B.substring(1));
 
}
}
