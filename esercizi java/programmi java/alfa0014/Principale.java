package alfa0014;

import java.util.*;

public class Principale {
    public static void main(String[] args) {// generazione di numeri randomici 
        int counter;
        Random rnum = new Random();
        /* below code would generate 10 random numebers
        between 0 and 100
         */
        System.out.println("random numebers generated below");
        for (counter=1; counter<=100; counter++){
            System.out.println(rnum.nextInt(100));
        }
    }
}