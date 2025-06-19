import java.util.Scanner;

class MediaNumeri{
	
	Scanner in = new Scanner(System.in);
	int a;
	float div;
	
	while(a<0){
		System.out.println("inserisci un numero");
		a=in.nxtInt();
		div=a/a;
	}
	System.out.println("la media e: "+div);
}