import java.util.Scanner;

class Quasiuguali{
	
	Scanner in = Scanner(System.in);
	
	String s="",s2="";
	
	System.out.println("inserisci due stringhe");
	s=in.nextLine();
	s2=in.nextLine();
	
	if(s.equals(s2)){
		System.out.println("sono uguali");
	}else if(s.equalsIgnoreCase){
				System.out.println("sono quasi uguali");
	}else {
		System.out.println("non sono uguali");
	}
}