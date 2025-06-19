import java.util.Scanner;

class ProgrammaInterattivo{
	
	Scanner sca =new Scanner(System.in);
	String string="";
	System.out.println("digita qualcosa e batti enter, oppure scrivi "+"fine"+" per terminare il progtamma");
	while(!(string= sca.next()).equals("fine")){
		System.out.println("hai digitato "+ string-toUpperCase()+ "!");
	}
	System.out.println("fine programma");
	
}