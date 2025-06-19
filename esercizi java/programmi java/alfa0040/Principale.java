package alfa0040;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
        int i, j;
        int mat1[][] = new int[3][3];
        int mat2[][] = new int[3][3];
        int mat3[][] = new int[3][3];
        Scanner scan = new Scanner(System.in);

        System.out.println("enter elements in first matrix: ");
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                mat1[i][j] = scan.nextInt();
            }
        }

        System.out.println("enter elements in second matrix: ");
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                mat2[i][j] = scan.nextInt();
            }
        }

        System.out.println("enter elements in third matrix: ");
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                mat3[i][j] = mat1[i][j] + mat2[i][j];
            }
        }

        System.out.println("the two matrix added successfully..!!\n");

        System.out.println("the new matrix will be: \n");
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                System.out.println(mat3[i][j] + " ");
            }
            System.out.println();
        }
    }
}
