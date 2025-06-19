import java.util.Scanner;

class AreaCerchio {
	
	Scanner in = Scanner(System.in);
	const float pi_greco=3.14;
	float area,raggio;
	System.out.println("inserisci il raggio");
	raggio=in.nextInt();
	area=pi_greco*raggio*raggio;
	System.out.println(area);
	
}