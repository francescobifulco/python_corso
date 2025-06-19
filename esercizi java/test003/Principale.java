package test003;

public class Principale {
	
	public static void main (String[] args){
		
		
		Persona p1 = new Persona();
		Persona p2 = new Persona();
		
		p1.nome = "pippo";
		p1.cognome = "paperino";
		
		p2.nome = "pluto";
		p2.cognome = "topolino";
		
		//p1.messaggio = "ciao";		
		Persona.messaggio = "ciao";		
		//System.out.println(p1.messaggio);
		//System.out.println(p2.messaggio);
		System.out.println(Persona.messaggio);
		
		
		
	}
	
}