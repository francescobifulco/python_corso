import java.util.Scanner;

class Asterischi{
	
	Scanner in = new Scanner(System.in);
	int a;
	
	System.out.println("inserisci un numero");
	a=in.nextInt();
	
	for(int i=0; i<=a; i++){
		System.out.print("*"+i);
	}
}