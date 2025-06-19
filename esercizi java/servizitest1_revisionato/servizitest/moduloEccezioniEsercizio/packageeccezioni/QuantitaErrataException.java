package packageeccezioni;

public class QuantitaErrataException extends Exception {
	
	public QuantitaErrataException() {
		super("il numero inserito non fa parte del range");
	}
	
}