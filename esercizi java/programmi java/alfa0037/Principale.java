package alfa0037;

import java.util.ArrayList;
import java.util.Collections;

public class Principale {
    public static void main(String[] args) {
        ArrayList<String> listOfInts = new ArrayList<String>();
        listOfInts.add("55");
        listOfInts.add("44");
        listOfInts.add("33");
        listOfInts.add("22");
        listOfInts.add("11");
        System.out.println("before reversing: "+listOfInts);
        Collections.reverse(listOfInts);
        System.out.println("after reversing: "+listOfInts);
    }
}
