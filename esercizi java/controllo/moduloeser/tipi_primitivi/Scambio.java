import java.util.Scanner;

class Scambio{
	
	Scanner in=new Scanner(System.in);
	int x,y;
	System.out.println("inserisci un numero: ");
    x=in.nextFloat();
	System.out.println("inserisci un numero: ");
    y=in.nextFloat();
	// inserisci i comandi mancanti qui
	int temp=x;
	x=y;
	y=temp;
	
	System.out.println("i numeri inserisci in modo inversci: ");
	System.out.println(x);
	System.out.println(y);
	
}