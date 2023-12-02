use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn main() {
    let input_num = 0;
    let input_paths = ["./input.txt", "./test_input.txt"];
    let input_data = read_lines(input_paths[input_num]);

    solve(&input_data);
}

fn solve(lines: &Vec<String>) {
    let mut p1_total = 0;
    let mut p2_total = 0;

    for line in lines {
        let colors = max_colors(line);
        if colors[1] <= 12 && colors[2] <= 13 && colors[3] <= 14 {
            p1_total += colors[0];
        }
        p2_total += colors[1] * colors[2] * colors[3];
    }

    println!("{}\n{}", p1_total, p2_total);
}

fn max_colors(line: &String) -> [i32; 4] {
    let mut output = [0, 0, 0, 0];
    let line: Vec<_> = line.split(": ").collect();

    let binding = line[1].replace(";", ",");
    let colors: Vec<_> = binding.split(", ").collect();

    output[0] = line[0][5..].parse().expect("Should be an int");

    for color in colors {
        let val_col: Vec<_> = color.split(" ").collect();
        let val = val_col[0].parse().expect("Should be a int");
        match val_col[1] {
            "red" => {
                if val > output[1] {
                    output[1] = val
                }
            }
            "green" => {
                if val > output[2] {
                    output[2] = val
                }
            }
            "blue" => {
                if val > output[3] {
                    output[3] = val
                }
            }
            &_ => todo!(),
        }
    }
    output
}
