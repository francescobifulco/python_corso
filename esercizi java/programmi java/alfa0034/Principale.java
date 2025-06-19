package alfa0034;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        int n,nu,num=0,rem;
        Scanner scan = new Scanner(System.in);
        System.out.println("enter any positive namber: ");
        n= scan.nextInt();

        nu=n;

        while (nu != 0) {
            rem=nu%10;
            num= num+rem*rem*rem;
            nu=nu/10;
        }
        if (num==n){
            System.out.println(n+" is an armstrong number");
        }
        else {
            System.out.println(n+" is not an armstrong number");
        }
    }
}