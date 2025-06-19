import java.util.Scanner;

class Consecutivi {
	
	Scanner in= new Scanner (System.in);
	int n;
		System.out.println("inseri i numeri");
n=in.nextInt();
if(n>2){
			System.out.println(" numero valido ");

}else{
			System.out.println(" numero non valido");

}

	int[] vetore= new int[n];
for(int i=0; i<=3;i++){
	if(vetore[i]==vetore[i]){
				System.out.println(" "+vetore[i]);

	}else{
				System.out.println("nessun valore");

	}
}


}
