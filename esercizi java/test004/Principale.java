package test004;

public class Principale {
			
	public static void main(String[] args) {
		
		Impiegato i1 = new Impiegato();
		i1.setReparto("imballaggio");
		i1.setStipendio(1000.00);		
		i1.setNome("pippo");
		i1.setCognome("paperino");
		i1.setEmail("uno@due.it");
		
		System.out.println(i1);
		
		
	}
	
}