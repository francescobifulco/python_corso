package alfa0028;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        float a,b,res;
        char choice,ch;
        Scanner scan = new Scanner(System.in);
        do {
            System.out.println("1 for addition\n");
            System.out.println("2 for subtraction\n");
            System.out.println("3 for multiplication\n");
            System.out.println("4 for diviono\n");
            System.out.println("5 for exitn\n\n");
            System.out.println("enter your choice: ");
            choice= Character.highSurrogate(scan.nextInt());
            switch (choice){
                case'1': System.out.println("enter two numbers: ");
                a=scan.nextFloat();
                b=scan.nextFloat();
                res=a+b;
                System.out.println("result "+a+" + "+b+" = "+res);
                break;
                case'2': System.out.println("enter two numbers: ");
                    a=scan.nextFloat();
                    b=scan.nextFloat();
                    res=a-b;
                    System.out.println("result "+a+" - "+b+" = "+res);
                    break;
                case'3': System.out.println("enter two numbers: ");
                    a=scan.nextFloat();
                    b=scan.nextFloat();
                    res=a*b;
                    System.out.println("result "+a+" * "+b+" = "+res);
                    break;
                case'4': System.out.println("enter two numbers: ");
                    a=scan.nextFloat();
                    b=scan.nextFloat();
                    res=a/b;
                    System.out.println("result "+a+" / "+b+" = "+res);
                    break;
                case '5': System.exit(0);
                    break;
                default: System.out.println("wrong choice!!!");
                    break;
            }
            System.out.println("\n--------------------------------------\n");
        }while (choice!=5);
    }
}
