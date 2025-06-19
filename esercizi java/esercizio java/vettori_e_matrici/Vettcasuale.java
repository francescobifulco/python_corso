import java.util.Random;

class Vettcasuale {
	final int dim_vett=8;
	final int min=10;
	final int max=100;
	
	int[] vetore= new int[dim_vett];

Random gen= new Random(2019);

for(int i=0; i<dim_vett;i++){
	vetore[i]=min+gen.nextInt((max-min)+1);
}
System.out.print("v= ");
for(int i=0;i<dim_vett;i++){
if(i>0;i<dim_vett;i++){
	System.out.print(", ");
	System.out.print(vetore[i]);
}
System.out.print();
}



	
}