package alfa0035;

public class Principale {
    int sum = 0;
    public int getNumbersum(int number){
        if (number==0){
            return sum;
        }
        else {
            sum +=(number%10);
            getNumbersum(number/10);
        }
        return sum;
    }

    public static void main(String[] args) {
        Principale numberSumRecsingRecursion = new Principale();
        System.out.println("sum of all digits of "+2234+" is: "+numberSumRecsingRecursion.getNumbersum(2234));
    }
}
