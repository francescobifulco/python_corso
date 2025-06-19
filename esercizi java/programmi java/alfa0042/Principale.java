package alfa0042;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        int ci ,i,j,k, l=0;
        String str,str1;
        char c,ch;
        Scanner scan =new Scanner(System.in);

        System.out.println("enter a string: ");
        str= scan.nextLine();

        i= str.length();
        for (c='A';c<='z';c++){
            k=0;
            //traversing 2 for loop here makes the complexity O(n2)
            for (j=0;j<i;j++){
                ch=str.charAt(j);
                if (ch==c){
                    k++;
                }
            }
            if(k>0){
                System.out.println("the character "+c+" has occurred for "+k+" times ");
            }
        }
    }
}



