
 /**
  *  Classe che astrae un <B>Marziano</B>.
  *  @author:Gianluca Tonti
  */ 
  public class Marziano{
  	
  	private String matricola;
  	private int autonomia;  //0..100
  	private int AI;         //0..10
  	private int tecnologia; //0..10
  	
  	/** 
  	 *  Costruttore che inizializza con valori di default 
     *  il marziano
     */   	
  	public Marziano(){
  		matricola = "indefinito";
  	    autonomia = 50;
  	    AI = 5;
  	    tecnologia = 5;
  	    System.out.println("Il Marziano " + matricola + " entra in gioco");
  	}
  		
  	/** 
  	 *  Costruttore che inizializza con i parametri passati per argomento
  	 *  il marziano
     */   	
  	
  	public Marziano (String nome, int[] parametri){
        matricola = nome;
  	    autonomia = parametri[0];
  	    AI = parametri[1];
  	    tecnologia = parametri[2];
        System.out.println("Il Marziano " + matricola + " entra in gioco");
  	}	
  	
   /** 
  	* Simulazione di un attacco.
  	*/  
  	public void attaccaTerrestri(){
  		
  		if (!attivo()) System.out.println("Non posso attaccare:Sono morto!");
        else {   		   		
  		      //algoritmo di attacco semplificato
  		      autonomia = autonomia - 20 + 2 * AI + tecnologia; 
  	    }      

  	}
  	
   /** 
  	* Restituisce <B>true</B> se ancora vivo, altrimenti <B>false</B>.
  	*/ 	
  	public boolean attivo(){
  	   if (autonomia > 0) return true;
  	   else return false;
  	   
  	}

 

   /** 
  	* Restituisce <B>true</B> se due oggetti marziani hanno la stessa autonomia,
  	* AI e tecnologia, altrimenti <B>false</B>.
  	*/ 	
	public boolean equals(Marziano x){
		if ((autonomia == x.autonomia) && (AI == x.AI) && (tecnologia == x.tecnologia)) return true;
		return false;
	}	
		 

 
  	public String toString () {
  		
  		return ("Sono il Marziano " + matricola + ". Autonomia: " + autonomia);
  	}   
  	
  } // Fine classe Marziano    	        