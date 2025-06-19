

public class GiocoBattaglia {
	
	

	public static void main(String args[]) {
		
		System.out.println("Ha inizio il Gioco...");
        
		int[] parametri_x102 = new int[3];
		parametri_x102[0]=50;
        parametri_x102[1]=5;
        parametri_x102[2]=5;
        
        int[] parametri_ken = {75,10,6};
		
		Marziano uno = new Marziano();
        Terrestre pippo = new Terrestre();
      
		Marziano x102 = new Marziano("X102", parametri_x102);
 	    Terrestre Ken = new Terrestre("Ken",parametri_ken);
   	      	    
   	   
   	    if (pippo.equals(Ken)) System.out.println(" ken e pippo sono uguali ");
   	    else System.out.println("pippo e' diverso da ken");
   	    
   	    // Nota! if (x102 == uno)... darebbe FALSE mentre (x102.equals(uno)) è TRUE!!!!
   	    // Perchè? Facoltativo: provare...
   	    if (x102.equals(uno)) System.out.println(" x102 e uno sono uguali ");
   	    else System.out.println("x102 e' diverso da uno");
   	       	     	   
   	    System.out.println("Prima dell'attacco. " + x102 + "\n" + Ken + "\n");

        

        for (int i=1;i<3;i++){
		    if (x102.attivo()) 
		    	    x102.attaccaTerrestri();

		    if (Ken.vivente()) 
		    	    Ken.attaccaMarziani();
           
           System.out.println("Dopo l'attacco "+ i + "\n" + x102 + "\n" + Ken + "\n");
		            
		    }              
	    		
	  System.out.println("Fine del Gioco");		

	}
}
