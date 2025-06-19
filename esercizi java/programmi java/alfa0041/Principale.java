package alfa0041;

public class Principale {
    public static void main(String[] args) {
        System.out.println("larrgest subbstring of hello world is: "+getLongestSubStringInString("hello world"));
    }
    private static String getLongestSubStringInString(String str) {
        String substr = "";
        String longestsubstr = "";
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (substr.indexOf(c) == -1) {
                substr += c;
                continue;
            } else {
                if (substr.length() > longestsubstr.length()) {
                    longestsubstr = substr;
                    substr = substr.substring(substr.indexOf(c) + 1) + c;
                }
            }
            if (substr.length()>longestsubstr.length()){
                longestsubstr=substr;
                return longestsubstr;
            }
        }
        return substr;
    }
}
