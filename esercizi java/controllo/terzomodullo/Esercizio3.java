import java.util.Scanner;

class Esercizio3 {//da vedere
	
	Scanner in =new Scanner(System.in);
	
	int dem;
	int[] vet= new int[dem];
	
	System.out.println("inserisci la dimensione");
	dem=in.nextInt();
	
	for(int i=0;i<=dem;i++){
		System.out.println("valori");
	    vet[dem]=in.nextInt();
		if(vet[i].length%2==0 && vet[i]>0){
		System.out.println("Tutti possitivi e pari");
	}
	else {
		System.out.println("NO");
	}
	}
	
}