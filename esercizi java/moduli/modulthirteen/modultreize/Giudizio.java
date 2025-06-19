package modultreize;

import java.util.Scanner;

public class Giudizio {
    public static void metodo12()  {
        Scanner in =new Scanner(System.in);
        int a;
        System.out.println("inserisci un voto");
        a=in.nextInt();
        if (a<0 && a>30){
            System.out.println("voto errore");
        }else if (a>=0 && a<=17){
            System.out.println("esame non superato");
        }else if (a>=18 && a<=24){
            System.out.println("suficiente");
        }else if (a>=25 && a<=30){
            System.out.println("buono");
        }
    }
}
