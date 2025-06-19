class Libro {

	int prezzo;
	String titolo, autore;
	public Libro(Sting a,String t, int p){
		autore=a;
		titolo=t;
		prezzo=p;
	}
	
	public Libro(Libro l){
		autore=l.getautore();
		titolo=l.gettitolo();
		prezzo=l.getprezzo();
	}
	
	public String getautore(){
		return autore;
	}
	
	public String gettitolo(){
		return titolo;
	}
	
	public int getprezzo(){
		return prezzo;
	}

}