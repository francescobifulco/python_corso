import java.util.Scanner;

class Esercizio2 {
	
	Scanner in =new Scanner(System.in);
	
	int kilo;
	float IMC,peso,altezza;
	
	System.out.println("inserisci il peso in kilo");
	kilo=in.nextInt();
	System.out.println("inserisci una altezza");
	altezza=in.nextFloat();
	
	peso=kilo;
	IMC=peso/(altezza*altezza);
	
	System.out.println("IMC"+IMC);
	System.out.println("la tua categoria");
	
	if(IMC<18.5){
		System.out.println("sottopeso");
	}
	if(IMC>=18.5 && IMC<25){
		System.out.println("peso normale");
	}
	if(IMC>=25 && IMC<30){
		System.out.println("sovrappeso");
	}
	if(IMC>=30){
		System.out.println("obeso");
	}
	
}