import java.io.*;
import java.util.*;

class Solve {
    public static void main(String[] args) {
        ArrayList<String> input = parseInput("input.txt");

        HashMap<String, Long> reg = new HashMap<>();
        reg.put("a", (long) 0);
        reg.put("b", (long) 0);
        part1and2(input, reg);

        reg.put("a", (long) 1);
        reg.put("b", (long) 0);
        part1and2(input, reg);
    }

    public static void part1and2(ArrayList<String> input, HashMap<String, Long> reg) {

        int i = 0;

        while (true) {
            if (i < 0 || i >= input.size()) {
                System.out.println(reg.get("b")); 
                break;
            }

            String[] inst = input.get(i).strip().split(",? ");

            if (inst[0].equals("hlf")) {reg.put(inst[1], reg.get(inst[1]) / 2); i++;}
            if (inst[0].equals("tpl")) {reg.put(inst[1], reg.get(inst[1]) * 3); i++;}
            if (inst[0].equals("inc")) {reg.put(inst[1], reg.get(inst[1]) + 1); i++;}

            if (inst[0].equals("jmp")) {i += Integer.parseInt(inst[1]);}

            if (inst[0].equals("jie")) {
                if (reg.get(inst[1]) % 2 == 0) {
                    i += Integer.parseInt(inst[2]);
                } else {i++;}
            }

            if (inst[0].equals("jio")) {
                if (reg.get(inst[1]) == 1) {
                    i += Integer.parseInt(inst[2]);
                } else {i++;}
            }
        }
    }

    public static ArrayList<String> parseInput(String filename){
        ArrayList<String> output = new ArrayList<String>(30);
        try {
            File myObj = new File(filename);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                
                output.add(data.strip());
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
