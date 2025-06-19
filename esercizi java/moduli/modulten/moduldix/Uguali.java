package moduldix;

import java.util.Scanner;

public class Uguali {
    public static void metodo9()  {
        Scanner in  = new Scanner(System.in);
        int a,b;
        System.out.println("inserisci due numeri");
        a= in.nextInt();
        b= in.nextInt();
        if (a==b){
            System.out.println("sono uguali");
        }
        else {
            System.out.println("non sono uguali");
        }
    }
}
