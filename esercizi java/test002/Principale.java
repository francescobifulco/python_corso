package test002;

public class Principale {
	
	public static void main(String[] args) {
		
		Cane c1 = new Cane();    // la variabile c1 è dichiarata come Cane, ed istanziata come Cane
		Animale c2 = new Cane(); // la variabile c2 è dichiarata come Animale, ed istanziata come Cane
		
		// intervallo di puntamento
		
		c1.abbaia();
		
		//c2.abbaia(); // errore, perchè l'intervallo di puntamento di c2 non ci consente di invocare il metodo abbaia()
						
		if (c2 instanceof Cane) {// mi domando : c2 è stato istanziato come Cane ? la risposta è si, quindi TRUE
			Cane c3 = (Cane) c2; // operazione di downcast			
			c3.abbaia();			
		}		
		
	}
	
}