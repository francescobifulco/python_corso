import java.util.Scanner;

class Percvoti{
	
	final int max_n=35;
	int n;
	int[] voti =new int[max_n]; 
	int somm=0,contsuff=0;contInsu=0;

Scanner in= new Scanner (System.in);

do{
		System.out.println("inserisci alunni: ");
		n=in.nextInt();
}while(n<1||n>max_n);
	
for(int i=0; i<n;i++){
	int v;
	boolean errore;
	do{
			System.out.println("voto dell alunno: "+i+1);
			v=in.nextInt();
			errore=(v<1||v>10);
			if(errore==true){
						System.out.println("voto non valido");	
			}
	}while(errore==true);
}
somm+=v;
if(v>=6){
	contsuff++;
}else{
	contInsu++;
	voti[i]=v;
}
				System.out.println("voto medio: "+(double)somm);
			System.out.println("percentuale suffici: "+100.0*contsuff);
			System.out.println("percentuale suffici: "+100.0*contInsu);

}