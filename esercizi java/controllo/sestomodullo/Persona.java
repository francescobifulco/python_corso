
class Persona {
	
	public int eta;
	public String nome,cognome;
	
	public Persona(String n,String c,int e){
		nome=n;
		cognome=c;
		eta=e;
	}
	
	public String dettagli(){
		return "il nome: "+nome+" il cognome: "+cognome+" eta: "+eta;
	}
	
}