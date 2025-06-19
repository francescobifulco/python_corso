
class Liberia{
	private Libro[] libri;
	
		public Liberia(Libro[] l){
		libri=new Libro[l.length];
		for(int i=0;i<l.length;i++){
			libri[i]=new Libro(l[i]);
		}
	}
	
	public int Trova(){
		int cont=0;
		String autore;
		System.out.println("inserisci autore");
		autore=getautore();
		int prezzo;
		System.out.println("inserisci prezzo");
		prezzo=getprezzo();
		for(int i=0;i<libri.length;i++){
			if (docenti[i].getautore().equals(a) && libri[i].getprezzo()>k){
				cont++;
			}
		}
		return cont;
}
}