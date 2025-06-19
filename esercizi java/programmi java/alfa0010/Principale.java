package alfa0010;

import java.io.IOException;
import java.util.Scanner;

public class Principale {
    public static void main(String[] args) throws NumberFormatException, IOException {// calcola il fatoriale 
        System.out.println("enter a number...");
        Scanner in = new Scanner(System.in);
        int number=in.nextInt();
        //call the recursive fuction to generate factorial
        int result = fact(number);
        System.out.println("factorial of the number is: "+ result);
    }

    static int fact(int b) {
        if (b<=1){
            //if the number is 1 then return 1
            return 1;
        }
        else {
            //else call the same function with the value-1
            return b*fact(b-1);
        }
    }
}