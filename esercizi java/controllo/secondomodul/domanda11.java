import java.util.Scanner;

class domanda11{
	Scanner in = new Scanner(System.in);
	int dem;
	int[] vet= new int[dem];
	
	System.out.println("dem");
	dem=in.nextInt();
	
	for (int i=0;i<vet.legth;i++){
		System.out.println("valori");
	    vet[dem]=in.nextInt();
	}
	
	int min,secondomin;
	 if (vet[0]<vet[1]){
		 min=vet[0];
		 secondomin=vet[1];
	 }
	 else {
		 min=vet[1];
		 secondomin=vet[0];
	 }
	 
	 for (int i=2;i<dem;i++){
		System.out.println("v["+i"]= ");
	    vet[1]=in.nextInt();
		if (vet[i]<min){
		 secondomin=min;
		 min=vet[i];
	 }
	 else if(v[i]<secondomin){
		 secondomin=v[i];
	 }
	} 
}