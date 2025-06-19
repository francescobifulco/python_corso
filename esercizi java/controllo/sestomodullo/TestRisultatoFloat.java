
class TestRisultatoFloat{
	
	float risultato= 5.0F;
	System.out.print(risultato);
	CambioRisultato r2 = new CambioRisultato();
	risultato = r2.cambioRisultato(risultato);
	
	System.out.print(risultato);
}