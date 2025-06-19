package alfa0008;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Principale {// converte i numeri decimali in numeri binari 
    public void convertbinary(int num){
        int binary[] = new int[40];
        int index = 0;
        while (num>0){
            binary[index++] = num%2;
            num= num/2;
        }
        for (int i=index-1; i>=0;i--){
            System.out.println(binary[i]);
        }
    }

    public static void main(String[] args) {
        Principale decimalToBinary = new Principale();
        System.out.println("Binary representation of 55: ");
        decimalToBinary.convertbinary(55);
        System.out.println("\nBinary representation of 45: ");
        decimalToBinary.convertbinary(45);
        System.out.println("\nBinary representation of 435: ");
        decimalToBinary.convertbinary(435);
    }
}