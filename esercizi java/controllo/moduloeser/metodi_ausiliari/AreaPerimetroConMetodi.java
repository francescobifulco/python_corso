import java.util.Scanner;

class AreaPerimetroConMetodi{
	
	public int areaRettangolo(int x,int y){
		 int a;
		 return a=x*y;
	}
	public int perimetroRettangolo(int x,int y){
		 int a;
		 return a=(x+y)*2;
	}
	
	public static void main (String[] args){
		
		Scanner in = new Scanner(System.in);
		
		int base,alterzza;
		System.out.println("inserisci base e alterzza");
		base=in.nextInt();
		alterzza=in.nextInt();
		
		System.out.println("area del rettangolo e: ");
		int area=areaRettangolo(base,alterzza);
		System.out.println(area);
		
		System.out.println("il perimetro del rettangolo e: ");
		int perimetro=perimetroRettangolo(base,alterzza);
		System.out.println(perimetro);
	}
}