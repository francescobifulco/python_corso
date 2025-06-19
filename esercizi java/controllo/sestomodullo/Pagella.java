import java.util.Arrays;

class Pagella {
	public Studente studente;
	public String[][] tabellaVoti;
	
	public Pagella(Studente stu, String[][] tab){
		studente=stu;
		tabellaVoti= tab;
	}
	
	public void StampaPagella(){
		System.out.println(Arrays.toString());
		System.out.println(Arrays.toString(tabellaVoti[1]));
		System.out.println(Arrays.toString(tabellaVoti[2]));
		System.out.println(Arrays.toString(tabellaVoti[3]));
		System.out.println(Arrays.toString(tabellaVoti[4]));
		System.out.println(Arrays.toString(tabellaVoti[5]));
		System.out.println(Arrays.toString(tabellaVoti[6]));
	}
}