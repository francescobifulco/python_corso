import java.util.Scanner;

class Equazioni{
	
	final double tolleranza= 1E-6;
	
	double a,b,c;
	double delta,x1,x2;
	
	Scanner in = new Scanner(System.in);
	
	System.out.println("inserisci i coefficienti dell equazione a*x^2+b*x+c=0");
	
	do{
		System.out.printl("a,b,c: ");
		a=in.nextDouble();
		b=in.nextDouble();
		c=in.nextDouble();

	}while(a==0);
	
	delta= Math.pow(b,2)-4.0*a*c;
	System.out.format("delta: "+delta);
	
	if(Math.abs(delta)<tolleranza){
		x1=-b/(2*a);
		System.out.format("x1=x2"+x1);
	}
	else if(delta>0){
		x1=(-b-Math.sqrt(delta))/(2*a);
		x2=(-b-Math.sqrt(delta))/(2*a);
	System.out.format("x1: "+x1+"x2: "+x2);
	}
	else{
		System.out.println("non esitono soluzioni reali");
	}
}