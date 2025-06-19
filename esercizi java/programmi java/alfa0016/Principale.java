package alfa0016;

import java.util.Arrays;

public class Principale {
    public static void main(String[] args) {// come unire due array in un array
        int[] array1 = {10,20,30};
        int[] array2 ={100,200,300};
        //print the two arrays whth for-loops
        int[] merge = new int [array1.length+array2.length];
        for (int i=0; i <array1.length;i++){
            merge[i]=array1[i];
        }
        for (int i=0; i <array2.length;i++){
            merge[i+array1.length]=array2[i];
        }
        //print the merge array
        System.out.println(Arrays.toString(merge));
    }
}