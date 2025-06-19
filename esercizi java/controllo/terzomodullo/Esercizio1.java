import java.util.Scanner;

class Esercizio1 {
	
	Scanner in =new Scanner(System.in);
	
	String a,b;
	System.out.println("inserisci una stringa");
	a=in.nextLine();
	System.out.println("inserisci una stringa");
	b=in.nextLine();
	System.out.println("la lunghezza della stringa: "+a.length()+" la stringa: "+a);
	System.out.println("la lunghezza della stringa: "+b.length()+" la stringa: "+b);
	
	String c;
	c=a +" "+b;
	System.out.println("la lunghezza della stringa: "+c.length()+" la strnga: "+c);
	
}