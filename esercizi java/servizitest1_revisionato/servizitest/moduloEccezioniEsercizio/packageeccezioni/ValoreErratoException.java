package packageeccezioni;

public class ValoreErratoException extends Exception {
	
	public ValoreErratoException() {
		super("il numero inserito non fa parte del range");
	}
}