package alfa0032;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("plaese enter a number to print fibonacci seres");
        int num = sc.nextInt();
        System.out.println("*******fibonacci seres*****");
        int f1,f2=0,f3=1;
        for (int i=1;i<=num;i++){
            System.out.println(" "+f3+" ");
            f1=f2;
            f2=f3;
            f3=f1+f2;
        }
    }
}
