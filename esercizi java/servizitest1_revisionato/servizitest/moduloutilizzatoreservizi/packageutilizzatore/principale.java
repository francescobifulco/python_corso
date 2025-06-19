package packageutilizzatore;

import java.util.ServiceLoader;
import serviziofferti.primoservizio;
import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;

public class principale{
	
	public static void main(String[] args){
		
		Iterable<primoservizio> servizitrovati = ServiceLoader.load(primoservizio.class);
		primoservizio servizio=servizitrovati.iterator().next();
		
	    servizio.stampaTabellina(6);

        int a;
		int r;
		a=5;
		r=servizio.fattoriale(a);
		System.out.println("il fattoriale di "+a+" vale "+r);
		
		int[] primoVettore = {4,6,8,2};
		boolean esito = servizio.soloPari(primoVettore);
		System.out.println("solo pari: " + esito);
		
		int[] secondoVettore = {3,9,5};
		esito = servizio.soloDispari(secondoVettore);
		System.out.println("solo dispari: " + esito);
		
		List<Integer> partenza = List.of(6, 4, 9, 2, 8, 4, 5, 8, 2, 2, 3, 4, 1, 9, 4, 7);
		List<Integer> arrivo = rimozioneDuplicati(partenza);//cannot find symbol
		System.out.println(arrivo);
		
	}
}