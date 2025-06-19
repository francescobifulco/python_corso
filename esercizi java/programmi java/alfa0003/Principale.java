package alfa0003;

import java.io.IOException;
import java.util.Scanner;

public class Principale {
    public static void main(String[] args) throws IOException {// controlla se il numero e un quadratto perfetto
        Scanner input = new Scanner(System.in);
        System.out.println("enter a number");
        //copying user input an integer variable named rows
        int number = input.nextInt();




        int sqrt= (int)Math.sqrt(number);
        if (sqrt*sqrt==number){
            System.out.println(number+" is a perfect square number!");
        }
        else {
            System.out.println(number+" is a not a perfect square number!");
        }
    }
}