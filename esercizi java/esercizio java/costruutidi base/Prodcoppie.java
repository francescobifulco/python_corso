import java.util.Scanner;

class Prodcoppie{

   int n;
   int pos=0,nullo=0,neg=0;
   
   Scanner in=new Scanner(System.in);
   
   System.out.printl("numero di coppie da inserire");
   n=in.nextInt();
   
   for(int i=1; i<=n; i++){
	   int a,b;
	   System.out.printl("coppia n: "+i);
	    a=in.nextInt();
		b=in.nextInt();
		if(a==0 || b==0){
			nullo++;
		}elseif((a>0 && b>0)||(a<0 && b<0)){
			pos++
		}else{
			neg++;
		}
		System.out.printl("numero di coppie da pos: "+pos);
		System.out.printl("numero di coppie da neg: "+neg);
		System.out.printl("numero di coppie da nullo: "+nullo);
   }
  
}