package test004;

public class Persona {
	
	private String nome, cognome, email;
		
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;		
	}
	
	public String getCognome() {
		return cognome;
	}
	
	public void setCognome(String cognome) {
		this.cognome = cognome;		
	}
	
	public String getEmail() {
		return email;
	}
	
	public void setEmail(String email) {
		this.email = email;		
	}
	
	@Override
	public String toString() {
		return "questa persona si chiama " + nome + " " + cognome + " e la sua email e': " + email;
	}
	
}