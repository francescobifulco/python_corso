package alfa0030;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        String str="1411";
        int num1=133;
        //convert string to integer
        int num2= Integer.parseInt(str);
        int sum= num1+num2;
        System.out.println("result of string after conversion to integer is : "+sum);

        String doublestr= "100.99";
        double d1=33.99;
        //convert string to double
        double d2 = Double.parseDouble(doublestr);
        double doublesum=d1+d2;
        System.out.println("result of string after conversion to double is : "+doublesum);


        //case does not matter for conversion
        String str2="true";
        //string to boolean conversion
        boolean bvar2=Boolean.parseBoolean(str2);
        System.out.println("boolean value of string is :"+bvar2);
    }
}
