package modulhuit;

import java.util.Scanner;

public class Grande {
    public static void metodo7()  {
        Scanner in = new Scanner(System.in);
        int a, b, c;
        System.out.println("inserisci tre numeri");
        a = in.nextInt();
        b = in.nextInt();
        c = in.nextInt();
        if (a > b) {
            System.out.println("il piu grande e: " + a);
        } else if (b > c) {
            System.out.println("il piu grande e: "+b);
        }
        else {
            System.out.println("il piu grande e: "+c);
        }
    }
}
