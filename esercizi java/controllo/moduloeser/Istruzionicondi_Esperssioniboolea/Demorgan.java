import java.util.Scanner;

class Demorgan{
	
	Scanner in = new Scanner(System.in);
	
	System.out.println("inserisci un numero");
	
	int num1=in.nextInt();
	int num2=in.nextInt();
	
	boolean num1pari=((num1%)==0);
	boolean num2pari=((num2%)==0);
	
	if((num1pari==%2) || (num2pari==0%2)){
		System.out.println("ii numeri sono entrambi pari");
	}
}