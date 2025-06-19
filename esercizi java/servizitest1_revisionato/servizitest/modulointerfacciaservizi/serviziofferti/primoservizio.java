package serviziofferti;

import java.util.ArrayList;
import java.util.Map;

public interface primoservizio{
	
	void stampaTabellina(int numero);
	int fattoriale(int numero);
	boolean soloPari(int[] vettore);
	boolean soloDispari(int[] vettore);
	ArrayList<Integer> rimozioneDuplicati(ArrayList<Integer> lista);
	Map<Integer, Integer> calcolaOccorrenze(ArrayList<Integer> lista);
	
	
	// ------------------------------------------------------------
	
	//ArrayList<Integer> rimozioneDuplicati(ArrayList<Integer> lista);
	// {6,2,9,2,6,8,9,8} -----> {6,2,9,8}
	// eccezione in caso venga rilevato un valore < 0
	
	//Map<Integer, Integer> calcolaOccorrenze(ArrayList<Integer> lista);
	// {6,2,9,2,6,8,9,8,8, 4}
	// eccezione in caso venga rilevato un valore < 0
	// ---------------------------------
	
	// C    V
	// 6	2
	// 2	2
	// 9	2
	// 8	3
	// 4	1
	
	
}