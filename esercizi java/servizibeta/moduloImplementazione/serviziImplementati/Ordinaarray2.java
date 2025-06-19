package serviziImplementati;

import serviziOfferti.PrimoServizio;
import java.util.Scanner;

public class Ordinaarray2 implements PrimoServizio {
	
	
	public int ordina(){
Scanner in = new Scanner(System.in);
        int[] array = new int [0];

        System.out.println("inserisci la dimensione del array");

        for (int i=0;i<array.length;i++){
            System.out.println(array);
        }
        //   array.Sort(array);
        System.out.println("array after sort");
        for (int j=0;j< array.length;j++){
            System.out.println(array);
        }
	}
	
}