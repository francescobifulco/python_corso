import java.util.Scanner;

class Stampamatr {
	
	Scanner in= new Scanner (System.in);
	int n,m;
	int[][] matrice =new int[n][m];
	
	for(int i=0;i<=3;i++){
		
if(n>0 ||n<1000){
	System.out.println("inseri i numeri");
n=in.nextInt();
}else{
	System.out.println(" numero non valido");
}
for(int j=0;j<4;j++){
	if(n>0 ||n<1000){
	System.out.println("inseri i numeri");
m=in.nextInt();
}else{
	System.out.println(" numero non valido");
}
}
	}
	System.out.println("rega: "+matrice[n][]+" colonne: "+matrice[][m]);

}
