import java.util.Scanner;

class ScrivoScrivoScrivo{
	
	Scanner in = new Scanner(System.in);
	int a;
	
		System.out.println("inserisci un numero");
		a=in.nextInt();
		
		if(a<0){
			System.out.println("error");
		}
		
		for(int i=0;i<=a;i++){
			System.out.println("sto ciclando");
		}
	
}