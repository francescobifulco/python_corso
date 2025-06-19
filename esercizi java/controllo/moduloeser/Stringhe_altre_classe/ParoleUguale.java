import java.util.Scanner;

class ParoleUguale{
	
	Scanner in = new Scanner(System.in);
	
	String a,b;
	
	System.out.println("inserisci una parola");
	a=in.nextLine();
	System.out.println("inserisci un parola");
	b=in.nextLine();
	
	if(a.equals(b)){
		System.out.println("sono uguali");
	}
	else{
		System.out.println("non sono uguali");
	}
	
}