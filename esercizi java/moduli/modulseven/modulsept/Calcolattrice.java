package modulsept;

import java.util.Scanner;

public class Calcolattrice {
    public static void metodo6()  {
        Scanner in = new Scanner(System.in);
        int a,x,y;
        int div=0,rest=0;
        System.out.println("inserisci un numero da 1 o 4");
        a= in.nextInt();
        switch (a){
            case 1: System.out.println("inserisci due numeri ");
            x= in.nextInt();
            y= in.nextInt();
            int som =x+y;
            System.out.println("la somma e: "+som);
            break;
            case 2: System.out.println("inserisci due numeri ");
                x= in.nextInt();
                y= in.nextInt();
                int sotra =x-y;
                System.out.println("la somma e: "+sotra);
                break;
            case 3: System.out.println("inserisci due numeri ");
                x= in.nextInt();
                y= in.nextInt();
                int mol=x*y;
                System.out.println("la somma e: "+mol);
                break;
            case 4: System.out.println("inserisci due numeri ");
                x= in.nextInt();
                y= in.nextInt();
                //eccezione della divisione 0/0
                try {
                    int c = x / y;
                    System.out.println(c);
                }catch (ArithmeticException exc){
                    System.out.println("la divisione he errata");}
                div=x/y;
                rest=x%y;
                System.out.println("il queziente della divisione e: "+div+" il resto e: "+rest);
                break;
            default: System.out.println("errore");
                break;
        }
    }
}
