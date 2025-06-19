import  java.util.Scanner;

class Esercizio6{
	
	Scanner in =new Scanne(System.in);
	int[] vet= new int[dem];
	int dem,m,som;
	
	System.out.println("dem");
	dem=in.nextInt();
	
	for (int i=0;i<vet.legth;i++){
		if(vet[i]<=1 || vet[i]>=10){
		System.out.println("voti da 1 a 10");
		vet[dem]=in.nextInt();
		som+=vet[i]+vet[i];
		m+=vet[i];
	    m=m/vet.length;
		}
		System.out.println(m);
	}
	
	int min,max;
	 if (vet[i]<vet[i]){
		 min=vet[i];
	 }
	 if(vet[i]<vet[i]){
		 max=vet[i];
	 }
	 
	 System.out.println("la media dei voti: "+m);
	 System.out.println("il minimo dei voti: "+min);
	 System.out.println("il massimo dei voti: "+max);
}