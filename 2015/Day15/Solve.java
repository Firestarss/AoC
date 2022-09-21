import java.io.*;
import java.util.*;
import java.util.Collections;

class Solve {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> input = parseInput("input.txt");
        ArrayList<ArrayList<Integer>> intCombos = generateIntCombos(input.size(), 100);

        part1and2(input, intCombos);
    }

    public static void part1and2(ArrayList<ArrayList<Integer>> data, ArrayList<ArrayList<Integer>> intCombos) {
        int p1MaxValue = 0;
        int p2MaxValue = 0;
        for (ArrayList<Integer> perm : intCombos) {
            ArrayList<Integer> properties = new ArrayList<Integer>(Collections.nCopies(5,0));
            
            for (int i = 0; i < perm.size(); i++) {
                properties.set(0, properties.get(0) + perm.get(i) * data.get(i).get(0));
                properties.set(1, properties.get(1) + perm.get(i) * data.get(i).get(1));
                properties.set(2, properties.get(2) + perm.get(i) * data.get(i).get(2));
                properties.set(3, properties.get(3) + perm.get(i) * data.get(i).get(3));
                properties.set(4, properties.get(4) + perm.get(i) * data.get(i).get(4));
            }


            int product = 1;
            for (int i = 0; i < 4; i++) {
                if (properties.get(i) < 0) {
                    product *= 0;
                }
                else {
                    product *= properties.get(i);
                }
            }

            if (product > p1MaxValue) {
                p1MaxValue = product;
            }

            if (product > p2MaxValue && properties.get(4) == 500) {
                p2MaxValue = product;
            }
        }
        System.out.println(p1MaxValue);
        System.out.println(p2MaxValue);
    }

    public static ArrayList<ArrayList<Integer>> generateIntCombos(int numValues, int total) {
        ArrayList<ArrayList<Integer>> output = new ArrayList<ArrayList<Integer>>(1000);

        // Base Case
        if (numValues == 1) {
            ArrayList<Integer> tempArr = new ArrayList<Integer>(1);
            tempArr.add(total);
            output.add(tempArr);

            return output;
        }

        for (int i = 0; i <= total; i++) {
            ArrayList<ArrayList<Integer>> tempArr = generateIntCombos(numValues - 1, total - i);
            
            for (ArrayList<Integer> subArray : tempArr) {
                subArray.add(i);

                output.add(subArray);
            }
        }

        return output;
    }

    public static ArrayList<ArrayList<Integer>> parseInput(String filename) {
        ArrayList<ArrayList<Integer>> output = new ArrayList<ArrayList<Integer>>(3);

        try {
            File file = new File(filename);
            Scanner sc = new Scanner(file);

            while (sc.hasNextLine()) {
                String nextLine = sc.nextLine();
                nextLine = nextLine.replaceAll("[^-0-9]+", " ");
                List<String> str_values = Arrays.asList(nextLine.trim().split(" "));
                ArrayList<Integer> int_values = new ArrayList<Integer>(3);
                for (String value : str_values) {
                    int_values.add(Integer.parseInt(value));
                }
                
                output.add(int_values);
            }
            sc.close();
        } catch (Exception e) {
            System.exit(1);
        }
        return output;
    }
}