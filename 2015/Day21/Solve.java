import java.util.*;
import java.io.*;

class Solve{
    public static void main(String[] args){
        int[][] weapons = new int[][]{
            { 8, 4, 0},  // Dagger
            {10, 5, 0},  // Shortsword
            {25, 6, 0},  // Warhammer
            {40, 7, 0},  // Longsword
            {74, 8, 0}}; // Greataxe

        int[][] armor = new int[][]{
            { 0, 0, 0},   // Dummy
            { 13, 0, 1},  // Leather
            { 31, 0, 2},  // Chainmail
            { 53, 0, 3},  // Splintmail
            { 75, 0, 4},  // Bandedmail
            {102, 0, 5}}; // Platemail

        int[][] rings = new int[][]{
            {  0, 0, 0},  // Dummy
            { 25, 1, 0},  // Damage +1
            { 50, 2, 0},  // Damage +2
            {100, 3, 0},  // Damage +3
            { 20, 0, 1},  // Defense +1
            { 40, 0, 2},  // Defense +2
            { 80, 0, 3}}; // Defense +3

        int[] bossStats = parseInput("input.txt");

        ArrayList<ArrayList<Integer>> allStats = genAllStats(weapons, armor, rings);

        part1(allStats, bossStats);

        Collections.reverse(allStats);
        part2(allStats, bossStats);
    }

    public static void part1(ArrayList<ArrayList<Integer>> allStats, int[] bossStats) {
        for (ArrayList<Integer> playerStats : allStats) {
            int playerTurns = (int) Math.ceil(100 / Math.max(bossStats[1] - playerStats.get(2), 1));
            int bossTurns = (int) Math.ceil(bossStats[0] / Math.max(playerStats.get(1) - bossStats[2], 1));

            if (playerTurns >= bossTurns) {
                System.out.println(playerStats.get(0));
                break;
            }
        }
    }

    public static void part2(ArrayList<ArrayList<Integer>> allStats, int[] bossStats) {
        for (ArrayList<Integer> playerStats : allStats) {
            int playerTurns = (int) Math.ceil(100 / Math.max(bossStats[1] - playerStats.get(2), 1));
            int bossTurns = (int) Math.ceil(bossStats[0] / Math.max(playerStats.get(1) - bossStats[2], 1));

            if (!(playerTurns >= bossTurns)) {
                System.out.println(playerStats.get(0));
                break;
            }
        }
    }

    public static ArrayList<ArrayList<Integer>> genAllStats(int[][] weapons, int[][] armor, int[][] rings) {
        ArrayList<ArrayList<Integer>> output = new ArrayList<ArrayList<Integer>>(7^4);

        for (int w = 0; w < weapons.length; w++) {
            for (int a = 0; a < armor.length; a++) {
                for (int r1 = 0; r1 < rings.length; r1++) {
                    for (int r2 = 0; r2 < rings.length; r2++) {
                        ArrayList<Integer> tempStats = new ArrayList<Integer>(3);
                        
                        if (r2 == 0 || r1 != r2) {
                            tempStats.add(weapons[w][0] + armor[a][0] + rings[r1][0] + rings[r2][0]);
                            tempStats.add(weapons[w][1] + armor[a][1] + rings[r1][1] + rings[r2][1]);
                            tempStats.add(weapons[w][2] + armor[a][2] + rings[r1][2] + rings[r2][2]);

                            output.add(tempStats);
                        }
                    }
                }
            }
        }

        output.sort(Comparator.comparingInt(e -> e.get(0)));

        return output;
    }

    public static int[] parseInput(String filename){
        int[] output = new int[3];
        try {
            File myObj = new File(filename);
            Scanner myReader = new Scanner(myObj);
            int i = 0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                
                output[i] = Integer.parseInt(data.substring(data.indexOf(":") + 2));
                i++;
            }
            myReader.close();
        } 
        catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return output;
    }
}