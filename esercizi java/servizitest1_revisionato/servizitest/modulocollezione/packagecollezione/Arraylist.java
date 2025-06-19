package packagecollezione;

import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import packageeccezioni.ValoreErratoException;


public class Arraylist {
	
	ArrayList<Integer> rimozioneDuplicati(ArrayList<Integer> lista){
		try{
			for(int elementi : lista)
				if(elementi<0){
				throw new ValoreErratoException();
			}
			List<Integer> risultato = new ArrayList<>();
		HashSet<Integer> l1 = new HashSet<Integer>(lista);
		List<Integer> list2 = new ArrayList<Integer>(l1);
		System.out.println("Elenco dopo la rimozione degli elementi duplicati:");
		for (Object ob : list2)
			System.out.println(ob);
			
		}catch(ValoreErratoException exc){
			System.out.println(exc.toString());
		}
        return risultato;//cannot find symbol
	}
}