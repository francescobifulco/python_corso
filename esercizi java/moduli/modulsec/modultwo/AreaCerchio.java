package modultwo;

import java.util.Scanner;

public class AreaCerchio {
    public static void metodo3() {
        
		final float pi=3.4f;
        Scanner in = new Scanner(System.in);
        float rag,are;
        System.out.println("inserisci il raggio");
        rag= in.nextInt();
        are=rag*rag*pi;
        System.out.println("area del cerchio e: "+are);
    
	}
}