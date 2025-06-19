import java.util.Scanner;
import java.util.String;

class Sottostring{
	
	Scanner in = new Scanner(System.in);
	
	String s="";
	
	do{
	System.out.println("inserire una stringa ");
	s=in.nextLine();
	
	}while(s.isEmpty()==true);
	int a,b;
	
	do{
	System.out.println("inserire due numeri ");
	a=in.nextInt();
	b=nextInt();
	
	
			
	}while(a<0 || a>b || b>s.lenght() );
	String s2=s.substring(a, b+1);
	System.out.println("sottostringa  "+s2);
}