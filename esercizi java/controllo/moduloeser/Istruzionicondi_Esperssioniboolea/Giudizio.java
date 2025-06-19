import java,util.Scanner;

class Giudizio{//da controllare
	
	Scanner in = new Scanner(System.in);
	int a;
	
	System.out.println("inserisci un voto");
	a=netxInt();
	
	if(a<=0 || a>=30){
		System.out.println("numero errato");
	}if else (a>=0 && a<=17){
		System.out.println("esame non passoto");
	}if else (a>=18 && a<=24){
		System.out.println("giudizio: sufficiente");
	}if else (a>=25 && a<=30){
		System.out.println("giudizio: buono");
	}
	
	boolean registra;
	if (a>=18 && a<=30){
		System.out.println("vuoi registrare il voto");
		registra=netxInt();//giustare
		registra==1;
		System.out.println("il voto e accettato");
		registra==1;
		System.out.println("il voto e stato rifiuttato");
	}
	
	
}