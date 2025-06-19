import java.util.Scanner;

class Parcheggio{

Scanner in= new Scanner(System.in);

float ore;
float costo_prima=2.50,costo_ore_succe=1.50,costo_tot=0.0f;

System.out.println("inserisci ore nel parcheggio");
	ore=in.nextFloat();
if(ore==1){
	ore=costo_prima;
	System.out.println("ore nel parcheggio: "+ore);
	System.out.println("costo nel parcheggio: "+costo_prima);
}
else if(ore>1){
	costo_tot=ore*costo_ore_succe;
	System.out.println("ore nel parcheggio: "+ore);
	System.out.println("costo nel parcheggio: "+costo_tot);
}
}