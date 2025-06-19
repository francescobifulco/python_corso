import java.util.Scanner;
import java.util.Random;

class Mescola{
	Scanner in = new Scanner(System.in);
	String s1="",s2="";
	
	System.out.println("inserisci una stringa");
	s1=in.nextLine();
	
	Random car = new Random();
	s1.CharArt(car);
	s2=s1;
	
	System.out.println(s2);
}