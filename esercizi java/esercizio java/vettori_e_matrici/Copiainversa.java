import java.util.Random;

class Copiainversa {
	final int dim_vett=15;
	final int min=-100;
	final int max=100;
	
	int[] vetore= new int[dim_vett];
	int[] vetoreb =new int[14];

Random gen= new Random(2019);

for(int i=0; i<dim_vett;i++){
	vetore[i]=min+gen.nextInt((max-min)+1);
}
System.out.print();
for(int i=0;i<=vetore.lenght();i++){
	if(vetore[i]>=0){
		vetoreb[i]=vetore[i];
	}
}
for(int i=0;i<vetoreb.lenght();i--){
	System.out.println(vetoreb[i]);
}
}
