package alfa0023;

import java.util.Arrays;

public class Principale {
    public static void main(String[] args) {// ordina gli elementi in un array 
        int [] array = {101,201,10,222};
        System.out.println("array elements before sort");
        for (int elem: array){
            System.out.println(elem);
        }
        // call array.sort on the int array
        Arrays.sort(array);
        System.out.println("array elements after sort ");
        for (int elem : array){
            System.out.println(elem);
        }
    }
}
