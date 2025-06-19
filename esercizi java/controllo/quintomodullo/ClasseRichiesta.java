
class ClasseRichiesta{
	
	public int numeroIntero;
	public NumeroIntero(int n){
		numeroIntero =n;
	}
	
	NumeroIntero uno = new NumeroIntero();
	NumeroIntero due = new NumeroIntero();
	uno.numeroIntero=1;
	due.numeroIntero=2;
	uno.stampaNumero();
	due.stampaNumero();
	
	public void stampaNumero(){
		System.out.println(numeroIntero);
	}
}