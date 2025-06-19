import java.util.Scanner;

class Ordina3Valori{//da contrllare
	
	Scanner in = new Scanner(System.in);
	int a,b,c,temp;
	
	System.out.println("inserisci un numero");
	a=nextInt();
	System.out.println("inserisci un numero");
	b=nextInt();
	System.out.println("inserisci un numero");
	c=nextInt();
	
    temp=a;
	a=b;
	b=temp;
	
}