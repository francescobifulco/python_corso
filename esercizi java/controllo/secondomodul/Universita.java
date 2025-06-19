
class Universita{
	private Docente[] docenti;
	
		public Universita(Docente[] d){
		docenti=new Docente[d.length];
		for(int i=0;i<d.length;i++){
			docenti[i]=new Docente(d[i]);
		}
	}
	
	
	public int etaMinima(){
		int min=docenti[0].geteta();
		for(int i=1;i<=docenti.length;i++){
		if(docenti[i].geteta()<min){
			min=docenti[i].geteta();
		}
	}
		return min;
	}
	
	public String[] TrovaGiovane(){
		String[] risultato;
		int cont=0;
		for(int i=0;i<docenti.length;i++){
			if (docenti[i].geteta()==etaMinima()){
				risultato=new String[cont];
				cont=0;
			}
		}
		for(int i=0;i<docenti.length;i++){
			if (docenti[i].geteta()==etaMinima()){
				risultato[i]=docenti[i].getcognome();
				cont++
			}
		}
		return risultato;
	}
}