import java.util.Scanner;

class mediamaggiore{


int dem; 

Scanner in= new Scanner (System.in);

for(int i=0;i<=5;i++){
System.out.println("inseri la dimensione");
dem=in.netxInt();
}

int medi=0,sum=0,max=0;
int[] vetore= new int[dem];


for(int i=0;i<vetore.lenght();i++){
	sum=sum+vetore[i];
	medi=sum/vetore.lenght();
	
	if(vetore[i]>max){
		max=vetore[i];
	}
}

System.out.println("la media: "+medi);
System.out.println("somma: "+sum);
System.out.println("il massimo: "max);

}