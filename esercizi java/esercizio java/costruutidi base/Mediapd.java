import java.util.Scanner;

class Mediapd{

 int medi=0,pari=0,disp=0,n=0,sum=0;
 
 Scanner in= new Scanner(System.in);
  System.out.printl("inserire un numeri da metere");
  n=in.nextInt();
 
 for(int i=0;i<=n;i++){
	 if(n%2==0){
		 sum=n+n;
		 medi=sum/n;
		 pari=medi;
	 }else if (n%2!=0){
		 sum=n+n;
		 medi=sum/n;
		 disp=medi;
	 }
 }

System.out.printl("la media pari: "+pari);
System.out.printl("la media disp: "+disp); 

}