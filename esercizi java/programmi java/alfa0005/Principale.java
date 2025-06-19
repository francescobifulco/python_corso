package alfa0005;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {// controlla se un numero e palindrome
        System.out.println("enter number....");
        Scanner in = new Scanner(System.in);
        int number= in.nextInt();
        int tempnum=number;
        int reversenumber=0;
        int temp=0;
        /*if the number is equal to it'is reversed number, then the given number
        is a palindrome number
        for example, 12221 is a palindrome number while 56 is not
         */
        // reverse the number
        while (number>0){
            temp=number%10;
            number=number/10;
            reversenumber=reversenumber*10+temp;
        }
        if (tempnum==reversenumber){
            System.out.println(tempnum+" is a palindreme number: ");
        }
        else {
            System.out.println(tempnum+" is not palindrome number: ");
        }
    }
}