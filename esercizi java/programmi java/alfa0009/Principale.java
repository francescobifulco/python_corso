package alfa0009;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Principale {// convertitore di temperatura 
    public static void main(String[] args) {
        float fah;
        double cel;
        Scanner scan =new Scanner(System.in);
        System.out.println("enter temperature in fahrenheit:" );
        fah= scan.nextFloat();
        cel= (fah-32)/1.8;
        System.out.println("equivalen temperature of "+cel+"in celsius="+cel );
        // convert centigrade to fahrenheit
        float cen;
        double fahre;
        Scanner scann = new Scanner(System.in);
        System.out.println("enter temperature in centigrade:");
        cen= scann.nextFloat();
        fahre=(1.8*cen)+32;
        System.out.println("equivalen temperature of "+fahre+"in celsius="+fahre );
    }
}