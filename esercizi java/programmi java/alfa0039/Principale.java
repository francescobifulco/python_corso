package alfa0039;

public class Principale {
    public void printtwomaxnumbers(int[] nums) {
        int maxone = 0;
        int maxtwo = 0;
        for (int n : nums) {
            if (maxone<n){
                maxtwo=maxone;
                maxone=n;
            } else if (maxtwo<n) {
                maxtwo=n;
            }
        }
        System.out.println("first max number: "+maxone);
        System.out.println("second max number: "+maxtwo);
    }
    public static void main(String[] args) {
        int num[]={531,34,88,2,45,133,991,234};
        Principale tmn=new Principale();
        tmn.printtwomaxnumbers(num);
    }
}
