package test004;

public class Impiegato extends Persona {
	
	private double stipendio;	
	private String reparto;
	
	public double getStipendio(){
		return stipendio;
	}
	
	public void setStipendio(double stipendio){
		this.stipendio=stipendio;
	}
	
	public String getReparto(){
		return reparto;
	}
	
	public void setReparto(String reparto){
		this.reparto=reparto;
	}
	
	@Override
	public String toString() {		
		String primaRiga = super.toString();
		String secondaRiga = "; questa persona e' anche un impiegato che guadagna " + stipendio + " euro e lavora al reparto " + reparto;		
		return primaRiga + secondaRiga;
	}
	
}