module moduloimplementazioneservizi{
	requires moduloEccezioniEsercizio;
	requires modulointerfacciaservizi;
	provides serviziofferti.primoservizio with serviziimplementati.primoservizioiml;
}