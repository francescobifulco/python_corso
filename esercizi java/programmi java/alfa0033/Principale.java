package alfa0033;

import java.util.Scanner;

public class Principale {
    public static void main(String[] args) {
      int  a,b,x,y,t,hcf,lcm;
      Scanner scsn = new Scanner(System.in);

      System.out.println("enter 2 numbers: ");
      x= scsn.nextInt();
      y= scsn.nextInt();

      a=x;
      b=y;

      while (b!=0){
          t=b;
          b=a%b;
          a=t;
      }

      hcf=a;
      lcm=(x*y)/hcf;

      System.out.println("hcf= "+hcf);
      System.out.println("\n lcm= "+lcm);
    }
}
