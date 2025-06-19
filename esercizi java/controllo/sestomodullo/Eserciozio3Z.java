
class Esercizio3Z{
	
	Studente studente1 = new Studente("Giovanni","Battista","5A");
	String[][] tabellaVoti1={{"ita","7","non si impegna troppo"},
	                        {"mat","9","e molto portato alla matematica"},
							{"sto","7","potrebbe fare di piu"},
							{"geo","8","appassionato"},
							{"ing","9","capace di sostenere dialoghi"},
							{"sci_mot","6","voto di incoraggiamento"},
                            {"mus","7","ha una certa passione nella materia"},};
					
    Pagella pagella1 = new Pagella(studente1,tabellaVoti1);
	
	Studente studente2 = new Studente("Giovanni","Battista","5A");
	String[][] tabellaVoti2={{"ita","7","non si impegna troppo"},
	                        {"mat","9","e molto portato alla matematica"},
							{"sto","7","potrebbe fare di piu"},
							{"geo","8","appassionato"},
							{"ing","9","capace di sostenere dialoghi"},
							{"sci_mot","6","voto di incoraggiamento"},
                            {"mus","7","ha una certa passione nella materia"},};
    Pagella pagella2 = new Pagella(studente2,tabellaVoti2);
	
	pagella1.stampaPagella();
	pagella2.stampaPagella();
}