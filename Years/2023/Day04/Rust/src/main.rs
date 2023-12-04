use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap() // panic on possible file-reading errors
        .lines() // split the string into an iterator of string slices
        .map(String::from) // make each slice into a string
        .collect() // gather them together into a vector
}

fn main() {
    let input_num = 0;
    let input_paths = ["./input.txt", "./test_input.txt"];
    let input_data = read_lines(input_paths[input_num]);

    solve(&input_data);
}

fn solve(lines: &Vec<String>) {
    let mut copies: HashMap<usize, usize> = HashMap::new();
    for i in 0..lines.len() {
        copies.insert(i, 1);
    }

    let mut p1_total = 0;
    let mut p2_total = 0;

    for (i, line) in lines.iter().enumerate() {
        let nums: Vec<_> = line.split(": ").collect::<Vec<_>>()[1]
            .split(" | ")
            .collect();

        let s1: HashSet<&str> = HashSet::from_iter(nums[0].split_whitespace());
        let s2: HashSet<&str> = HashSet::from_iter(nums[1].split_whitespace());

        let intersection = s1.intersection(&s2).count();

        if intersection > 0 {
            p1_total += 2_usize.pow((intersection - 1) as u32);
        }

        for j in 0..intersection {
            let cur_copies = copies.get(&i).expect("Value should be present").clone();
            *copies.entry(i + j + 1).or_default() += cur_copies;
        }
    }

    for copy in copies {
        p2_total += copy.1;
    }

    println!("{}\n{}", p1_total, p2_total);
}
