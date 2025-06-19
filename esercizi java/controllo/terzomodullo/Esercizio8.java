import  java.util.Scanner;

class Esercizio6{
	
	Scanner in =new Scanne(System.in);
	int[] vet= new int[dem];
	int dem,m,som,suff=0,grave=0;
	
	System.out.println("inserisci le materie");
	dem=in.nextInt();
	
	for (int i=0;i<vet.length;i++){
		System.out.println("inserisci i voti: ");
		vet[dem]=in.nextInt();
		som+=vet[i]+vet[i];
		m+=vet[i];
	    m=m/vet.length;
		System.out.println(m);
		if(vet[i]>=6){
			suff++;
		}
		else if(vet[i]<4){
			grave++;
		}
	}
	if(suff==vet[i].length){
		System.out.println("esito promosso");
	}
	else if(grave!=0){
		System.out.println("respinto");
	}
	else if(vet[i].length-suff<=3){
		System.out.println("esito sospeso in: "+(vet[i].length-suff)+" materie");
	}
	else{
		System.out.println("respinto");
	}
	
}