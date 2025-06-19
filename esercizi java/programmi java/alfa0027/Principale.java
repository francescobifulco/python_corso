package alfa0027;

import java.util.Scanner;
import java.util.ArrayList;

public class Principale {
    public static void main(String[] args) {
        /*creation of arralist: */
        ArrayList<String> list = new ArrayList<String>();
        /*this is how elements should be added to the array list*/
        list.add("Raj");
        list.add("Abhit");
        list.add("Vivek");
        list.add("Shiva");
        list.add("Arun");

        /*displaying array list elements*/
        System.out.println("currently the array list has following elements: "+list);

        /*add elements at the given index*/
        list.add(0, "Bider");
        list.add(1,"Arun");
        System.out.println("currently the array list has following elements after adding: "+list);
        /*remove elements form array list like this*/
        list.remove("omm");
        list.remove("sun");

        System.out.println("currently the array list elements after after removing elements are: "+list);

        /*remove elements form the given index*/
        list.remove(1);

        System.out.println("currently the array list elements after after removing elements from first position are: "+list);
    }
}