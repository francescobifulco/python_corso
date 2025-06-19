package alfa0046;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        int size,i,j,temp;
        int arr[] = new int[20];
        Scanner scan = new Scanner(System.in);

        System.out.println("enter the array size: ");
        size = scan.nextInt();

        System.out.println("enter array elements and press enter: ");
        for (i=0; i<size;i++){
            arr[i] = scan.nextInt();
        }
        //now j will point to the last element
        j= i-1;
        //and i will point to the fist element
        i=0;

        while (i<j){
            temp = arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
            i++;
            j--;
        }

        System.out.println("now printing the reverse of array is: \n");
        for (i=0;i<size;i++){
            System.out.println(arr[i]+" ");
        }
    }
}
