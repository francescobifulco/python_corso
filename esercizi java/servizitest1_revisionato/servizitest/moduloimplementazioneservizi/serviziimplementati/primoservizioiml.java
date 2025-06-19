package serviziimplementati;

import serviziofferti.primoservizio;
import packageeccezioni.ValoreErratoException;
import packageeccezioni.QuantitaErrataException;

public class primoservizioiml implements primoservizio{
		
	@Override
	public void stampaTabellina(int numero) {
		try{
			if(numero>10){
				throw new ValoreErratoException();
			}
			for(int i=1; i<=10; i++)
				System.out.println(i*numero);
		}catch(ValoreErratoException exc){
			System.out.println(exc.toString());
		}	
	}
	
	@Override
    public int fattoriale(int numero){		
		int f=1;		  
		try{
			if(numero<0){
				throw new ValoreErratoException();
			}
			for(int i=1; i<=numero; i=i+1)
				f=f*i;
		}catch(ValoreErratoException exc){
			System.out.println(exc.toString());
		}
		return f;		
	}
	
	@Override
    public boolean soloPari(int[] vettore){
		boolean epari = true;
        try{
			if(vettore.length<1 || vettore.length>20){
				throw new QuantitaErrataException();
			}
			for(int i=0; i<vettore.length; i++)
				if(vettore[i]%2!=0) {
					epari=false;
					break;
				}  
		}catch(QuantitaErrataException exc){
			System.out.println(exc.toString());
		}		  
		return epari;		
	}
	
	@Override
    public boolean soloDispari(int[] vettore){
		boolean edisp = true;
        try{
			if(vettore.length<1 || vettore.length>20){
				throw new QuantitaErrataException();
			}
			for(int i=0; i<vettore.length; i++)
				if(vettore[i]%2==0){
					edisp=false;
					break;
				}	
		}catch(QuantitaErrataException exc){
			System.out.println(exc.toString());
		}	
		return edisp;
	}
	
	@



	
}
