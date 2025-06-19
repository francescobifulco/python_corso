package alfa0026;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        int n,i,sum=0,armean;
        int arr[]= new int[50];
        Scanner scan = new Scanner(System.in);

        System.out.println("how many number you want to enter? ");
        n=scan.nextInt();

        System.out.println("enter "+n+" numbers: ");
        for (i=0;i<n;i++){
            arr[i]=scan.nextInt();
            sum=sum+arr[i];
        }
        armean=sum/n;
        System.out.println("arithmetic mean= "+armean);
    }
}
