package alfa0024;

public class Principale {
    public static void main(String[] args) {// scambia i valori delle variabili 
        int num1 = 144;
        int num2 = 255;
        System.out.println("before swapping");
        System.out.println("value of num1: " + num1);
        System.out.println("value of num2: " + num2);
        // swap the value
        swap(num1,num2);

        System.out.println("\n\n\n");

        //swap two varable without using third varable
        int num3 = 33;
        int num4 = 44;
        System.out.println("before swapping");
        System.out.println("value of num3: " + num3);
        System.out.println("value of num4: " + num4);
        // add both the numbers and assing it to first
        num3=num3+num4;
        num4=num3-num4;
        num3=num3-num4;
        System.out.println("after swapping");
        System.out.println("value of num3: " + num3);
        System.out.println("value of num4: " + num4);
    }
    private static void swap( int num1, int num2){
        int temp = num1;
        num1 = num2;
        num2 = temp;
        System.out.println("after swapping");
        System.out.println("value of num1: " + num1);
        System.out.println("value of num2: " + num2);
    }
}
