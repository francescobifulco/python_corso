package alfa0029;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Scanner;
import java.util.function.IntFunction;

public class Principale {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();

        list.add("1111");
        list.add("2222");
        list.add("3333");
        list.add("4444");

        String [] countries = list.toArray(new String[list.size()]);
        System.out.println("elements in array are below ");
        for( String element:countries){
            System.out.println(element);
        }
    }
}
