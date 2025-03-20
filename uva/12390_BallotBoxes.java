package uva;


// the judge doesn't accept my answer but uDebug says that
// my outputs is identical to the accepted output so idk what to do :/

import java.util.Scanner;
import java.util.PriorityQueue;

class BallotBoxes {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        while (true) {
            int n = scan.nextInt();
            int b = scan.nextInt();

            if (n == -1) {
                break;
            }

            PriorityQueue<double[]> pq = new PriorityQueue<>((x, y) -> {
                if (x[0] != y[0]) {
                    return Double.compare(-x[0], -y[0]);
                }
                return Double.compare(x[1], y[1]);
            });


            int population;
            int[] boxes = new int[500000];

            for (int i = 0; i < n; i++) {
                population = scan.nextInt();
                double[] city = {population, population, i};
                boxes[i] = 1;
                pq.add(city);
            }

            b -= n;

            while (b > 0) {
                double[] curr = pq.poll();
                int city = (int) curr[2];
                boxes[city] += 1;
                double[] newcity = {curr[1]/boxes[city], curr[1], curr[2]};
                pq.add(newcity);
                b -= 1;
            }


            double res = pq.poll()[0];
            if (res == (int) res) {
                System.out.println((int) res);
            } else {
                System.out.println((int) res + 1);
            }
        }

        scan.close();
    }
}
