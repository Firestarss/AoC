import java.io.*;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Collections;

class Solve {
    public static void main(String[] args) {
        int[][] lights = parseInput("input.txt");

        part1(lights);
        part2(lights);
    }

    public static void part1(int[][] lights) {
        for (int i = 0; i < 100; i++) {
            lights = step(lights);
        }
        int sum = 0;
        for (int[] r : lights) { 
            for (int c : r) {
                sum += c;
            }
        }

        System.out.println(sum);
    }

    public static void part2(int[][] lights) {
        int[][] corners = {{0,0}, {99,0}, {0,99}, {99,99}};

        for (int[] corner : corners) {
            lights[corner[0]][corner[1]] = 1;
        }

        for (int i = 0; i < 100; i++) {
            lights = step(lights);

            for (int[] corner : corners) {
                lights[corner[0]][corner[1]] = 1;
            }
        }
        int sum = 0;
        for (int[] r : lights) { 
            for (int c : r) {
                sum += c;
            }
        }

        System.out.println(sum);
    }

    public static int[][] step(int[][] lights) {
        int[][] output = new int[100][100];

        for (int i = 0; i < lights.length; i++) {
            for (int j = 0; j < lights[i].length; j++) {
                int adjTotal = adj(lights, i, j);

                if (lights[i][j] == 1) {
                    output[i][j] = 0;
                    if (adjTotal == 2 || adjTotal == 3) {
                        output[i][j] = 1;
                    }
                }
                else {
                    output[i][j] = 0;
                    if (adjTotal == 3) {
                        output[i][j] = 1;
                    }
                }
            }
        }
        return output;
    }

    public static int adj(int[][] lights, int x, int y) {
        int output = 0;
        int[][] neighbors = {{1,0}, {0,1},
                             {-1,0}, {0,-1},
                             {1,1}, {-1,-1},
                             {1,-1}, {-1,1}};

        for (int[] neighbor : neighbors) {
            int nx = neighbor[0] + x;
            int ny = neighbor[1] + y;

            if (nx < lights.length && nx >= 0 && ny < lights[0].length && ny >= 0 &&
                lights[nx][ny] == 1) {
                    output++;
                }
        }
        return output;
    }

    public static int[][] parseInput(String filename) {
        int[][] output = new int[100][100];

        try {
            File file = new File(filename);
            Scanner sc = new Scanner(file);
            int i = 0;

            while (sc.hasNextLine()) {
                String nextLine = sc.nextLine().trim();
                
                for (int j = 0; j < nextLine.length(); j++) {
                    if (nextLine.charAt(j) == '#') {
                        output[i][j] = 1;
                    }
                    else {
                        output[i][j] = 0;
                    }
                }
                i++;
            }
        } catch (Exception e) {
            System.exit(1);
        }
        return output;
    }
}