
 /**
  *  Classe che astrae un <B>Terrestre</B>.
  *  @author:Gianluca Tonti
  */ 
  public class Terrestre{
  	
  	private String nome;
  	private int vita;       //0..100
  	private int velocita;   //0..10
  	private int armamento;  //0..10
  	
  	/** 
  	 *  Costruttore che inizializza con valori di default 
     *  il terrestre
     */   	
  	public Terrestre(){
  		nome = "sconosciuto";
  	    vita = 50;
  	    velocita = 5;
  	    armamento = 5;
  	    System.out.println("Il Terrestre " + nome + " entra in gioco");
  	}
  		
  	/** 
  	 *  Costruttore che inizializza con i parametri passati per argomento
  	 *  il terrestre
     */   	
  	
  	public Terrestre (String denominazione, int[] parametri){
        nome = denominazione;
  	    vita = parametri[0];
  	    velocita = parametri[1];
  	    armamento = parametri[2];
        System.out.println("Il Terrestre " + nome + " entra in gioco");
  	}	
  	
   /** 
  	* Simulazione di un attacco.
  	*/  
  	public void attaccaMarziani(){
  		
  		if (!vivente()) System.out.println("Non posso attaccare:Sono morto!");
        else {                		   		
  		      //algoritmo di attacco semplificato
  		      vita = vita - 20 + 2 * velocita + armamento;   		      
  	    }      

  	}
  
   /** 
  	* Restituisce <B>true</B> se ancora vivo, altrimenti <B>false</B>.
  	*/    	
  	public boolean vivente(){
  	   if (vita > 0) return true;
  	   else return false;
  	}

  
  /** 
  	* Restituisce <B>true</B> se due oggetti  hanno la stessa vita,
  	* velocita e armamento, altrimenti <B>false</B>.
  	*/ 	  	
	public boolean equals(Terrestre x){
	 if ((vita == x.vita) && (velocita == x.velocita) && (armamento == x.armamento)) return true;
     return false;  	
	}	
	
  
  
  
  	public String toString () {
  		return ("Terrestre " + nome + ". Vita: " + vita);
  	}   
  	
  } // Fine classe Terrestre    	        