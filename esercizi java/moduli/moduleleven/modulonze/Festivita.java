package modulonze;

import java.util.Scanner;

public class Festivita {
    public static void metodo10()  {
        Scanner in = new Scanner(System.in);
        int a,b;
        System.out.println("inserisci un giorno ");
        a=in.nextInt();
        if (a<=31){
            System.out.println("giorno correto");
        }
        else {
            System.out.println("giorno non correto");
        }
        System.out.println("inserisci un mese ");
        b=in.nextInt();
        if (b<=12){
            System.out.println("mese correto");
        }
        else {
            System.out.println("mese non correto");
        }
        if (a==31 && b==12){
            System.out.println("capodanno");
        } else if (a==6 && b==1) {
            System.out.println("epifania");
        } else if (a==15 && b==8) {
            System.out.println("feragosto");
        } else if (a==25 && b==12) {
            System.out.println("natale");
        }
        else {
            System.out.println("non e una festivita");
        }
    }
}
