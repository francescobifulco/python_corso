package alfa0004;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {// vede se un numore e primo o non lo e
        int num,i,count=0;
        Scanner scan = new Scanner(System.in);
        System.out.println("enter a number: ");
        num = scan.nextInt();
        for (i=2;i<num;i++){
            if (num%i==0){
                count++;
                break;
            }
        }
        if (count==0){
            System.out.println(num+" is a prime number");
        }
        else {
            System.out.println(num+" is not a prime number");
        }
    }
}