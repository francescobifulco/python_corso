package alfa0025;

import java.util.Scanner;
public class Principale {
    public static void main(String[] args) {//?
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter a number to calculate sum of digits");
        int number = sc.nextInt();
        //remember numbers /10 reduces one digit from number // and number%10
        //gives yuo last digit
        int sum = 0;
        int input = number;
        while (input!=0){
            int lastdigit = input%10;
            sum+=input%10;
            sum +=lastdigit;
            input/=10;
        }
        System.out.println("sum of digits of number "+number+" is " + sum);

    }
}