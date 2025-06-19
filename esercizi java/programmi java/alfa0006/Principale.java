package alfa0006;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) { // costruisce una mezza piramide con i numeri 
        int rows,number=1,counter,j;
        //to get the user's input
        Scanner input = new Scanner(System.in);
        System.out.println("enter the number of rows for flyd's triangle: ");
        //copying user input into an integer variable named rows
        rows=input.nextInt();
        System.out.println("floyd's triangle");
        System.out.println("*****************");
        for (counter=1;counter<=rows;counter++){
            for (j=1;j<=counter;j++){
                System.out.println(number+"");
                //incrementing the number value
                number++;
            }
            //for new line
            System.out.println("");
        }
    }
}
