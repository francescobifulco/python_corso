
public class StatoGioco{

 static private int contatoreTerrestri = 0;
 static private int contatoreMarziani = 0;
 
 public static void incMarziani(){
 	  contatoreMarziani += 1;
 }	    
 

public static void incTerrestri(){
 	  contatoreTerrestri += 1;
 }	    
 
public static int numTerrestriinGioco(){
 	  return contatoreTerrestri;
 }	    

public static int numMarzianiinGioco(){
 	  return contatoreMarziani;
 }	    

}