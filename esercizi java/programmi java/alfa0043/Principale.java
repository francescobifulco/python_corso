package alfa0043;

import java.util.Locale;

public class Principale {
    public static void main(String[] args) {
        Locale locale = Locale.getDefault();

        System.out.println(locale.getDisplayLanguage());
        System.out.println(locale.getDisplayCountry());

        System.out.println(locale.getLanguage());
        System.out.println(locale.getCountry());

        System.out.println(System.getProperty("user.country"));
        System.out.println(System.getProperty("user.language"));
    }
}
