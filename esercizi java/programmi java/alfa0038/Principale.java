package alfa0038;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        //declare the original string object
        String strorig = "string to character array convert";
        //declare the char array
        char[] stringarray;
        //convert string into array using tochararray() method of string class
        stringarray= strorig.toCharArray();
        //disply the array
        System.out.println("character array elements are below-------");
        for (int index=0;index<stringarray.length;index++){
            System.out.println(stringarray[index]);
        }
    }
}