package alfa0002;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {// controlla se anno bisestile
        //year we want to check
        System.out.println("enter a year to check if it is leap or not...");
        Scanner in = new Scanner(System.in);
        int year = in.nextInt();
        // if year is divisible by 4, it is a leap year
        if ((year%400==0)||((year%4==0) && (year%100!=0))){
            System.out.println("year "+year+"is a leap year ");
        }
        else {
            System.out.println("year"+year+" is not a leap year ");
        }
    }
}