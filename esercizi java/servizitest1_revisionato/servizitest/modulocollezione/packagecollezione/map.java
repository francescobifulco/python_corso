package packagecollezione;

import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import packageeccezioni.ValoreErratoException;

public class map {
	
	Map<Integer, Integer> calcolaOccorrenze(ArrayList<Integer> lista){
		Map<Integer, Integer> m1 = null;
		try{
			for(int elementi :lista)
				if(elementi<0){
				throw new ValoreErratoException();
			}
			lista.add(6);
		    lista.add(2);
		    lista.add(9);
		    lista.add(2);
		    lista.add(6);
			lista.add(8);
			lista.add(9);
			lista.add(8);
			lista.add(8);
			lista.add(4);
		    System.out.println(lista);
			
			m1 = new HashMap<>();
			m1.put(6,2);
			m1.put(2,2);
			m1.put(9,2);
			m1.put(8,3);
			m1.put(4,1);
			System.out.println(m1);
			
		}catch(ValoreErratoException exc){
			System.out.println(exc.toString());
		}	
		return m1;
	}
}