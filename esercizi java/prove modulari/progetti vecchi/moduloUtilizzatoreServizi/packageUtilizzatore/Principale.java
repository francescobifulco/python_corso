package packageUtilizzatore;

import java.util.ServiceLoader;
import serviziOfferti.PrimoServizio;

public class Principale {
	
	public static void main(String[] args) {
		
		Iterable<PrimoServizio> serviziTrovati = ServiceLoader.load(PrimoServizio.class); // cestino
		
		PrimoServizio servizioScelto = serviziTrovati.iterator().next(); // prendi il riferimento al primo (ed unico) modulo trovato
				
		int risultato = servizioScelto.somma(5, 7);		
		System.out.println(risultato); // 12
		
		risultato = servizioScelto.sottrazione(15, 7);		
		System.out.println(risultato); // 8
		
	}
	
}