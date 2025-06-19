import java.util.Random;


class TestaCroce {
	int testa=0;
    int croce=1;
	Random r = new Random();
	boolean ok= r.nextBoolean();
	if (testa==ok){
		System.out.println("testa");
	}
	else {
		System.out.println("croce");
	}	
}