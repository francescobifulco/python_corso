import java.util.Scanner;

class Rimpiazza {
	
	Scanner in = new Scanner(System.in);
	String frase;
	
	System.out.println("inserisci una frase");
	frase=in.nextLine();
	
	String par_sost;
	System.out.println("inserisci la parola da sostituire");
	par_sost=in.nextLine();
	
	frase.replaceAll(par_sost,frase);
	System.out.println(frase);

}