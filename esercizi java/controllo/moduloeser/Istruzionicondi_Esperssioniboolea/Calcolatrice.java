import java,util.Scanner;

class Calcolatrice{
	
	Scanner in = new Scanner(System.in);
	int x,y,a;
	
	System.out.println("inserisci un numero compreso da 1 a 4 (1 somma), (2 sotrazzione), (3 moltiplicazione), (4 divisione)");
	a=netxInt();
	switch (a){
		case 1: 
		System.out.println("inserisci due numero");
		x=netxInt();
		y=netxInt();
		int som;
		som+=x+y;
		System.out.println("il risultato"+som);
		break;
		
		case 2:
		System.out.println("inserisci due numero");
		x=netxInt();
		y=netxInt();
		int sotr;
		sotr=x-y;
		System.out.println("il risultato"+sotr);
		break;
		
		case 3:
		System.out.println("inserisci due numero");
		x=netxInt();
		y=netxInt();
		int molt;
		molt=x*y;
		System.out.println("il risultato"+molt);
		break;
		
		case 4:
		System.out.println("inserisci due numero");
		x=netxInt();
		y=netxInt();
		int div,que;
		div=A/B;
	System.out.println("il quoziente della divisione"+div);
	que=A%B;
	System.out.println("il resto della divisione"+que);
		break;
		
		default: System.out.println("error");
		
	}
	
	
}