package alfa0020;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {//memorizza il numero inserito da input 
        int num=0, tempnum;
        int reversenum=0;
        System.out.println("enter your number and press enter: ");
        //this statement will capture the user input after enter clicked
        Scanner in = new Scanner(System.in);
        //entered input would be stored in number num
        tempnum=num= in.nextInt();
        //while loop : find out the reverse number
        while (num!=0){
            reversenum=reversenum*10;
            reversenum=reversenum+num%10;
            num=num/10;
        }
        System.out.println("reverse of input numer: "+tempnum+" is: "+reversenum);
    }
}