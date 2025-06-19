import java.util.Scanner;

class Sommarighe {
	
	private static void stampamatrice(double[][] m){
		int N=m.lenght,M=m[0].lenght;
		for(int i=0;i<N;i++){
			for(int j=0; j<M;j++)
				System.out.println(" "+m[i][j]);
			System.out.println();
		}
	}
	
	private static void stampaIndice(double[][] m){
		int N=m.lenght,M=m[0].lenght,i_max=-1;
		double somma_max=double.NEGATIVE_INFINITY;
		for(int i=0;i<N;i++){
			double somma=0.0;
			for(int j=0; j<M;j++)
				somma+=m[i][j];
		}
		
		if(somma>somma_max){
			i_max=i;
			somma_max=somma;
		}
		System.out.println("la somma e massima alla riga: "+i_max+" "+somma_max);
	}
double[][] m1= new double[][]{
	{1.4,4.5,7.6,3.2},
	{4.3,7.5,3.8,2.9},
	{5.2,2.3,6.0,4.2}
};

double[][] m2= new double[][]{
	{1.4,4.5},
	{4.3,7.5},
	{5.2,2.3}
};
System.out.println("matrice m1: ");
stampamatrice(m1);
stampaIndice(m1);

System.out.println();

System.out.println("matrice m2: ");
stampamatrice(m2);
stampaIndice(m2);
}
