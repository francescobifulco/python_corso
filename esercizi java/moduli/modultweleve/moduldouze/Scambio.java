package moduldouze;

import java.util.Scanner;

public class Scambio {
   public static void metodo11()  {
        Scanner in =new Scanner(System.in);
        int x,y,temp=0;
        System.out.println("inscerisci due numeri");
        x= in.nextInt();
        y= in.nextInt();
        temp=x;
        x=y;
        y=temp;
        System.out.println("ordine");
        System.out.println(x);
        System.out.println(y);
    }
}
