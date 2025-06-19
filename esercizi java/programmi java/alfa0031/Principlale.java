package alfa0031;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        int decnum,rennum,quot,i=1,j;
        int octnum[]= new int[100];
        Scanner scan = new Scanner(System.in);

        System.out.println("enter any decimal number: ");
        decnum = scan.nextInt();

        quot=decnum;

        while (quot!=0){
            octnum[i++]=quot%8;
            quot=quot/8;
        }

        System.out.println("equivalent ocal value of "+decnum+" is:\n");
        for (j=i-1;j>0;j--){
            System.out.println(octnum[j]);
        }

        //binary to decimal
        int binnum,decinum=0,i1=1,rem;
        Scanner scann = new Scanner(System.in);

        System.out.println("enter binary number: ");
        binnum = scann.nextInt();
        int binnumtemp=binnum;

        //converting the number into decimal format
        while (binnum !=0){
            rem=binnum%10;
            decinum=decinum+rem*i1;
            i1=i1*2;
            binnum=binnum/10;
        }
        System.out.println("equivalent decimal value of "+binnumtemp+" is:\n");
        System.out.println(decinum);

        //decimal to hexadecimal
        int decimnum,remnum;
        String hexdecnum="";

        /*digits in hexadecimal numner system */
        char hex[]= {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};

        Scanner scanne = new Scanner(System.in);

        System.out.println("enter decimal number: ");
        decimnum= scanne.nextInt();
        int orgnum=decimnum;

        while (decimnum>0){
            remnum=decimnum%16;
            hexdecnum=hex[remnum]+hexdecnum;
            decimnum=decinum/16;
        }
        System.out.println("equivalent hexadecimal value of "+orgnum+" is:\n");
        System.out.println(hexdecnum);
    }
}
