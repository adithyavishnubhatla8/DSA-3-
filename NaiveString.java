 public class NaiveStringMatching {
    public static void naiveSearch(String a, String b) {
        int n = a.length();
        int m = b.length();
        for (int i = 0; i <= n - m; i++) {
            int j;
            for (j = 0; j < m; j++) {
                if (a.charAt(i + j) != b.charAt(j)) {
                    break;
                }
            }
            if (j == m) {
                System.out.println("Pattern found at index " + i);
            }
        }
    }
    public static void main(String[] args) {
        String text = "ABABABCABABAB";
        String pattern = "ABAB";
        naiveSearch(a, b);
    }
}