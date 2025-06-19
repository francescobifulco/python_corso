package serviziImplementati;

import serviziOfferti.PrimoServizio;

public class PrimoServizioImpl implements PrimoServizio {
	
	@Override
	public int somma(int a, int b) {
		return a + b;
	}
	
	@Override
	public int sottrazione(int a, int b) {
		return a - b;
	}
	
}