package modul;

import java.util.Scanner;
import modulcinq.NomeCognome;
import modulquatre.Divisione;
import modultwo.AreaCerchio;
import modulsixx.PerimetroTriangolo;
import modultri.AreaTriangolo;
import modulsept.Calcolattrice;
import modulhuit.Grande;
import modulneuf.Ugualisenzaelse;
import moduldix.Uguali;
import modulonze.Festivita;
import moduldouze.Scambio;
import modultreize.Giudizio;



public class Principale {
   
   public static void main(String[] args) {
         Scanner in= new Scanner(System.in);
       int a = 0;
       System.out.println("scegli un tra 1 a 12");
       a=in.nextInt();

        switch (a){
            case 1: NomeCognome.metodo1();
            break;
            case 2: Divisione.metodo2();
            break;
			case 3: AreaCerchio.metodo3();
            break;
			case 4: PerimetroTriangolo.metodo4();
            break;
			case 5: AreaTriangolo.metodo5();
            break;
			case 6: Calcolattrice.metodo6();
            break;
			case 7: Grande.metodo7();
            break;
			case 8: Ugualisenzaelse.metodo8();
            break;
			case 9: Uguali.metodo9();
            break;
			case 10: Festivita.metodo10();
            break;
			case 11: Scambio.metodo11();
            break;
			case 12: Giudizio.metodo12();
            break;
			default:System.out.println("errore");
            break;
        
		}
    }
}