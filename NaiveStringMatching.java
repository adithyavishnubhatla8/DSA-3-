 public class NaiveStringMatching {
    public static void naiveSearch(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        for (int i = 0; i <= n - m; i++) {
            int a;
            for (a = 0; a < m; a++) {
                if (text.charAt(i + a) != pattern.charAt(a)) {
                    break;
                }
            }
            if (a == m) {
                System.out.println("Pattern found at index " + i);
            }
        }
    }
    public static void main(String[] args) {
        String text = "ABABABCABABAB";
        String pattern = "ABAB";
        naiveSearch(text, pattern);
    }
}