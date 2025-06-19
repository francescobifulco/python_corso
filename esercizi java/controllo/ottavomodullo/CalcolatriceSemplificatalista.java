
import java.util.Scanner;

class CalcolatriceSemplificatalista{
		Scanner in = new Scanner(System.in);
	int x,y,a;
	

	System.out.println("inserisci un numero compreso da 1 a 8 (1 somma), (2 sotrazzione), (3 moltiplicazione), (4 divisione), (5 restuire il resto), (6 restiuire il piu grande numero) (7 restituire numero piu piccolo), (8 restituire la media tra due numeri)"));
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
		int div;
		div=x/y;
	    System.out.println("il quoziente della divisione"+div);
		break;
		
		case 5:
		System.out.println("inserisci due numero");
		x=netxInt();
		y=netxInt();
		int que;
		que=x%y;
	    System.out.println("il resto della divisione"+que);
		
		case 6:
		System.out.println("inserisci due numero");
		x=netxInt();
		y=netxInt();
		int max;
		if (x<y){
			max=x;
		}
		System.out.println("il massimo: "+max);
		
		case 7:
		System.out.println("inserisci due numero");
		x=netxInt();
		y=netxInt();
		int min;
		if (x>y){
			min=x;
		}
		System.out.println("il massimo: "+min);
		
		case 8:
		System.out.println("inserisci due numero");
		x=netxInt();
		y=netxInt();
		int med;
		med=x+y/2;
		System.out.println("il massimo: "+max);
		
		default: System.out.println("error");
	}