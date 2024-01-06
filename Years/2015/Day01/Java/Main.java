import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {

    public static void part1(String data) {
        long countOpen = data.chars().filter(c -> c == '(').count();
        long countClose = data.chars().filter(c -> c == ')').count();
        System.out.println(countOpen - countClose);
    }

    public static void part2(String data) {
        int floor = 0;
        for (int i = 0; i < data.length(); i++) {
            char c = data.charAt(i);
            floor = c == '(' ? floor + 1 : floor - 1;
            if (floor < 0) {
                System.out.println(i + 1);
                break;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Path path = Paths.get("../input.txt");
        String data = Files.readString(path);
        part1(data);
        part2(data);
    }
}
