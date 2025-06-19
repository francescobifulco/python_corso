import  java.util.Scanner;

class Esercizio6{
	
	Scanner in =new Scanne(System.in);
	int[] vet= new int[dem];
	int dem;
	
	System.out.println("dem");
	dem=in.nextInt();
	
	for (int i=0;i<vet.legth();i++){
		System.out.println("inserisci le temperature");
		vet[dem]=in.nextInt();
		if(vet[i].legth()<=20){
			System.out.println("inferiore"+vet[i]);
		}
		else if ( vet[i].legth>=20){
			System.out.println("superiore"+vet[i]);
		}
		else if ( vet[i].legth==20){
			System.out.println("uguale"+vet[i]);
			}
	}
	System.out.println("buona settimana");
}