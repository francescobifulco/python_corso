
class Strudente{
	public String nome, cognome;
	public String classe;
	public String[] materie={4,5,6,3};
	
	public studente(String n,String c, String cl){
		nome=n;
		cognome=c;
		classe=cl;
	}
	
	public String stampaalunno(){
		return System.out.println("nome: "+nome+" cognome: "+cognome+" classe: "+classe);
	}
	
	public String stampavoti(){
		return System.out.println("ita: "+materie[0]+" mat: "+materie[1]+" sto: "+materie[2]+" art: "+materie[3]);
	}
}