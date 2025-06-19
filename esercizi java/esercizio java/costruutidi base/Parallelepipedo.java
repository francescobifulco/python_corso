import java.util.Scanner;

class Parallelepipedo{
	
	Scanner in = new Scanner(System.in);
	
	float largh,alte,lungh,valume,areatot;
	float Abas,Alat;
	
	System.out.println("inserisci la larghezza");
	largh=in.nextFloat();
	System.out.println("inserisci la altezza");
	alte=in.nextFloat();
	System.out.println("inserisci la lunghezza");
	lungh=in.nextFloat();
	
	Abas=lungh*largh;
	Alat=2*(lungh+largh)*alte;
	valume=lungh+largh+alte;
	areatot=Alat+2*Abas;
	
	System.out.println("il volume: "+valume);
	System.out.println("area totale: "+areatot);
	
}