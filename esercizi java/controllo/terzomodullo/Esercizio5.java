import java.util.Scanner;

class Esercizio5 {
	
	Scanner in =new Scanne(System.in);
	String alfabeto="abcdefghijklmmnopqrstuvwxyz";
	String crittoStr=" ";
	String cont="s";
	String s;
	System.out.println("inserisci un messaggio: ");
	s=in.nextLine();
	int index;
	int chiave;
	System.out.println("inserisci il salto: ");
	chiave=in.nextInt();
	chiave=(chiave%alfabeto.length());
	char at;
	for(int i=0;i<s.length();i++){
		at=s.charAt(i);
		if(alfabeto.contains(at+" ")){
			index=alfabeto.indexOf(at);
			index=(index+chiave)%alfabeto.length();
			at=alfabeto.charAt(index);
		}
		crittoStr+=at;
	}
	System.out.println("messaggio crittografatto: "+crittoStr);
}