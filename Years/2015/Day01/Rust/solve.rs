use std::fs;

fn part1(data: &str) {
    let count_open = data.chars().filter(|&c| c == '(').count();
    let count_close = data.chars().filter(|&c| c == ')').count();
    println!("{}", count_open - count_close);
}

fn part2(data: &str) {
    let mut floor = 0;
    for (i, c) in data.chars().enumerate() {
        floor = if c == '(' { floor + 1 } else { floor - 1 };
        if floor < 0 {
            println!("{}", i + 1);
            break;
        }
    }
}

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Unable to read file");
    part1(&data);
    part2(&data);
}
