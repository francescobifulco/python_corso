package alfa0000;

import java.util.Arrays;

public class Principale {
    public static void main(String[] args) {//fa la somma degli elementi in un array
        //define an array and intialise with values
        int[] numbers = new int[] {22,20,41,55,16,60,100};
        /*averge value of array elements would de
        sum of all elements /total number of elements
         */
        //calculate sum of all array elements
        int sum=0;
        for (int i=0; i<numbers.length;i++){
            sum=sum+numbers[i];
            //calculate average value
            float average=sum/numbers.length;
            System.out.println("averge is :"+ average);
        }
    }
}