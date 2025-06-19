package alfa0019;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {// stampa la tabelina del numero inserito da input 
        int num,tab;
        Scanner scan = new Scanner(System.in);
        System.out.println("entrer number: ");
        num = scan.nextInt();
        System.out.println("table of "+ num+"is\n");
        for (int i=1; i<=10;i++){
            tab=num*i;
            System.out.println(num+"*"+i+"="+tab+"\n");
        }
    }
}