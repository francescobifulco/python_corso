import java.util.Scanner;
import java.util.Random;

class Esercizio{
	
	Scanner in= new Scanner(System.in);
	int[][] vet= new int[5][4];
	int som=0;
	
	System.out.println("la matrice: ");
	for(int i=0;i<=5;i++){
		System.out.println("\t");
		for(int j=0;j<4;j++){
			vet[i][j]=(int)(Math.random()*100);
			if(vet[i][j]%2==0 && vet[i][j]%3==0){
				som+=vet[i][j];
				System.out.println(" "+vet[i][j]);
			}
			System.out.println("\t");
		}
		System.out.println("la somma e: "+som);
	}	
}