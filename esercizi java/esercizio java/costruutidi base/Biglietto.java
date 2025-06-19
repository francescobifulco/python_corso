import java.util.Scanner;

class Biglietto{
	final double per_scon_pensonati=0.10;
	final double per_scon_studenti=0.15;
	final double per_scon_disocupati=0.25;
	
	double perscoto;
	double costoinizio,sconto,costofinale;
	char categoria;
	
	Scanner in= new Scanner(System.in);
	
	System.out.println("costo iniziale del utente");
	costoinizio=in.nextDouble;
	
	System.out.println("P-pensionati");
	System.out.println("S-studenti");
	System.out.println("D-disocupato");
	System.out.println("altro tasto - applicazione della tariffa piena");
	System.out.println("categoria: ");
	
	categoria=in.next().toUpperCase().charAt(0);
	Switch(categoria){
		case 'P':perscoto=per_scon_pensonati;
		break;
		
		case 'S':perscoto=per_scon_studenti;
		break;
		
		case 'D':perscoto=per_scon_disocupati;
		break;
		
		default: 
		perscoto=0.0;
	}
	sconto=perscoto*costoinizio
	costofinale=costoinizio-sconto;
	
	System.out.println("costo iniziale: "+costoinizio);
	System.out.println("sconto applicazione: "+sconto);
	System.out.println("costo finale: "+costofinale);
	
}