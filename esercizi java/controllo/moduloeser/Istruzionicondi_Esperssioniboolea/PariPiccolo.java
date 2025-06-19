import java.util.Scanner;

class PariPiccolo {
	
	Scanner in = new Scanner(System.in);
	int A;
	System.out.println("inserisci un numero");
	A=nextInt();
	if (A==0%2 && (A>=0) && (A<=100) ){
		System.out.println("il numero e pari e piccolo: "+A);
	}else{
		System.out.println("il numero non e pari e piccolo: "+A);
	}
	
} 