package alfa0001;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {// calcola il fatoriale di 3
        System.out.println("enter a number...");
        Scanner in =new Scanner(System.in);
        int number= in.nextInt();
        //factorial of any number in !n. For example, factorial of 3 is 3*2*1
        int factorial=number;
        for (int i=(number-1); i>1; i--){
            factorial=factorial*i;
        }
        System.out.println("factorial of the number is: "+number+" is: "+factorial);
    }
}