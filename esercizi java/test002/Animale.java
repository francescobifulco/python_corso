package test002;

public abstract class Animale {
	
	public String nome;
	public double peso;
	
	public void mostraInformazioni() {
		System.out.println("questo animale si chiama " + nome + " e pesa " + peso + " kg");
	}
	
}