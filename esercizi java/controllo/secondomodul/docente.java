
class Docente {

	int eta,codice;
	String nome, cognome;
	public Docente(Sting n,String c, int e, int cd){
		nome=n;
		cognome=c;
		codice=cd;
		eta=e;
	}
	
	public Docente(Docente d){
		nome=d.getnome();
		cognome=d.getcognome();
		codice=d.getcodice();
		eta=d.geteta();
	}
	
	public String getnome(){
		return nome;
	}
	
	public String getcognome(){
		return cognome;
	}
	
	public int getcodice(){
		return codice;
	}
	
	public int geteta(){
		return eta;
	}
	
	

}