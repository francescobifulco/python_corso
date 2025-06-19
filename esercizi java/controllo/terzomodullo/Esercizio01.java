import java.util.Scanner;

class Esercizio01 {
	
	Scanner in =new Scanner(System.in);
	String frase;
	String parola;
	
	System.out.println("inserisci una frase");
	frase=in.nextLine();
	
	System.out.println("inserisci una parola");
	parola=in.nextLine();
	
	int sum=0,i=0,x;
	do{
		x=frase.indexOf(parola,i);
		if(x!=-1){
			sum++;
			i=x+1;
		}
	}while(x!=-1);
	
	System.out.println("la stringa "+parola+" e presente"+sum);	
}