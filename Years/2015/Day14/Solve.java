import java.io.*;
import java.util.*;
import java.util.Collections;

class Solve {
    public static void main(String[] args) {
        ArrayList<Reindeer> reindeer1 = gen_reindeer_list();
        ArrayList<Reindeer> reindeer2 = gen_reindeer_list();
        
        part1(reindeer1);
        part2(reindeer2);
    }

    public static void part1(ArrayList<Reindeer> reindeer) {
        for (int i = 0; i < 2503; i++) {
            for (Reindeer deer : reindeer) {
                deer.move();
            }
        }

        ArrayList<Integer> scores = new ArrayList<Integer>(reindeer.size());
        for (Reindeer deer : reindeer) {
            scores.add(deer.getDistance());
        }
        System.out.println(Collections.max(scores));
    }

    public static void part2(ArrayList<Reindeer> reindeer) {
        ArrayList<Integer> scores = new ArrayList<>(Arrays.asList(new Integer[reindeer.size()]));
        Collections.fill(scores, 0);
        int maxDistance = 0;

        for (int i = 0; i < 2503; i++) {
            for (Reindeer deer : reindeer) {
                deer.move();
            }

            maxDistance = 0;
            for (Reindeer deer : reindeer) {
                if (deer.getDistance() > maxDistance) {
                    maxDistance = deer.getDistance();
                }
            }

            for (int j = 0; j < reindeer.size(); j++) {
                if (reindeer.get(j).getDistance() == maxDistance) {
                    scores.set(j, scores.get(j) + 1);
                }
            }
        }

        System.out.println(Collections.max(scores));
    }

    public static ArrayList<Reindeer> gen_reindeer_list() {
        ArrayList<Reindeer> reindeer = new ArrayList<Reindeer>(5);

        try {
            File file = new File("input.txt");
            Scanner sc = new Scanner(file);

            while (sc.hasNextLine()) {
                String nextLine = sc.nextLine();
                nextLine = nextLine.replaceAll("[^0-9]+", " ");
                List<String> values = Arrays.asList(nextLine.trim().split(" "));
                List<Integer> int_values = new ArrayList<Integer>(3);
                for (String value : values) {
                    int_values.add(Integer.parseInt(value));
                }
                
                reindeer.add(new Reindeer(int_values.get(0),int_values.get(1),int_values.get(2)));
            }
            sc.close();
        } catch (Exception e) {
            System.exit(1);
        }
        return reindeer;
    }
}