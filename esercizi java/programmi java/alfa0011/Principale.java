package alfa0011;

public class Principale {
    public static void main(String[] args) {// associare i numeri in un array dal piu piccola al maggiore 
        // array of 10 numbers
        int numbers[]= new int[]{88,99,67,12,98,77,98,12,21};
        //assing first element of an array to largest and smallest
        int smallest=numbers[0];
        int largest =numbers[0];
        for (int i=1; i<numbers.length;i++){
            if (numbers[i]>largest){
                largest=numbers[i];

            }
            else if (numbers[i]<smallest){
                smallest=numbers[i];
            }
            System.out.println("largest number is "+largest);
            System.out.println("smallest number is "+smallest);
        }
    }
}
