import java.util.Scanner;

class Divisione {
	
	Scanner in = Scanner(System.in);
	int A,B,div,que;
	System.out.println("inserisci un numero");
	A=in.nextInt();
	System.out.println("inserisci un numero");
	B=in.nextInt();
	div=A/B;
	System.out.println("il quoziente della divisione"+div);
	que=A%B;
	System.out.println("il resto della divisione"+que);
	
}