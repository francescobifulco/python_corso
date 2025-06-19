package alfa0018;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {// stampare un elenco di numeri senza i primi numeri 
        int i=0;
        int num=0;
        //empty string
        String primenumbers="";
        System.out.println("input your number to which you want to print all prime numbers and press enter:");
        //this statement will capture the user input
        Scanner in = new Scanner(System.in);
        int boundrynum= in.nextInt();;
        for (i=1;i<=boundrynum;i++) {
            int convert = 0;
            for (num = i; num >= 1; num--) {
                if (i % num == 0) {
                    convert = convert + 1;
                }
            }
            if (convert==2){
                System.out.println(i+"is a prime number");
            }
        }
    }
}
