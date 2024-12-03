import java.util.*;

public class s2_averageprimes {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = 2000000;
        int inp;
        boolean[] primes = new boolean[n+1];
        Arrays.fill(primes, true);
        primes[0] = false;
        primes[1] = false;
        // Arrays.fill(nameofarr, False);
        for (int i = 2; i < (int) Math.sqrt(n); i++) {
            if (primes[i]) {
                for (int j = i*2; j < n; j += i) {
                    primes[j] = false;
                }
            }
        }
        ArrayList<Integer> al = new ArrayList<Integer>();
        for (int i = 0; i < primes.length; i++) {
            if (primes[i]) {
                al.add(i);
            }
        }

              
        int t = scan.nextInt();
        for (int a = 0; a < t; a++) {
            inp = scan.nextInt();
            for (int b = 0; b < al.size(); b++) {
                if (primes[al.get(b)] && primes[2*inp-al.get(b)]) {
                    System.out.println(al.get(b) + " " + (2*inp-al.get(b)));
                    break;
                }
            }
        }
        scan.close();
    }
}