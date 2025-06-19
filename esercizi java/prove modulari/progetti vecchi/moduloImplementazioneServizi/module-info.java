module moduloImplementazioneServizi {
	
	requires moduloInterfacciaServizi;
	provides serviziOfferti.PrimoServizio with serviziImplementati.PrimoServizioImpl;
	
}