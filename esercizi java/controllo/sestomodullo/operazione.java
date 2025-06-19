
 class operazione {
	 double[] r1 = new double[];
	 int[] r2 = new int[];
	 float[] r3 = new float[];
	 double[] r4 = new double[];
	 
	 double div;
	 int a=5,b=3;
	 div=(double)a/b;
	 r1[0]=div;
	 
	 int molt;
	 char c='a';
	 short s=5000;
	 molt=c*s;
	 r2[0]=molt;
	 
	 float som;
	 int i=6;
	 float f=3.14F;
	 som+=i+f;
	 r3[0]=som;
	 
	 double sotr;
	 sotr=r1[0]-r2[0]-r3[0];
	 r4[0]=sotr;
	 
	 System.out.println(molt+" "+r2[0]);
	 System.out.println(div+" "+r1[0]);
	 System.out.println(som+" "+r3[0]);
	 System.out.println(sotr+" "+r4[0]);
 }