import java.util.Scanner;

class Esercizio4 {
	
	Scanner in =new Scanne(System.in);
	String s
	System.out.println("inserisci una frase");
	s=in.nextLine;
	for(int i=0; i<s.lenght();i++){
		char c=s.charAt(i);
		switch(c){
			case'a':case'e':case'i':case'o':case'u':
			case'A':case'E':case'I':case'O':case'U':
			System.out.print(c);
			break;
		}
	}
	System.out.println();
}