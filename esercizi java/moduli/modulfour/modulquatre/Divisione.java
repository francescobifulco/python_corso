package modulquatre;

import java.util.Scanner;

public class Divisione {
   
   public static void metodo2()  {
   
        Scanner in = new Scanner(System.in);
        int a,b,div=0,rest=0;
        System.out.println("inserisci primo numero");
        a= in.nextInt();
        System.out.println("inserisci secondo numero");
        b= in.nextInt();
        //eccezione della divisione 0/0
        try {
            int c = a / b;
            System.out.println(c);
        }catch (ArithmeticException exc){
        System.out.println("la divisione he errata");}
        div=a/b;
        rest=a%b;
        System.out.println("il queziente della divisione e: "+div+" il resto e: "+rest);

    }
}
