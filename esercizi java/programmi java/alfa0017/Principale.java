package alfa0017;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Principale {
    public static void main(String[] args) {// stampare orario
        Date dnow = new Date();
        SimpleDateFormat ft1 = new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat ft2 = new SimpleDateFormat("E");
        SimpleDateFormat ft3 = new SimpleDateFormat("hh:mm:ss a");
        SimpleDateFormat ft4 = new SimpleDateFormat("MMM");
        System.out.println("the current date is: "+ft1.format(dnow));
        System.out.println("today is: "+ft2.format(dnow));
        System.out.println("the current time is: "+ft3.format(dnow));
        System.out.println("the current month name is: "+ft4.format(dnow));
    }
}