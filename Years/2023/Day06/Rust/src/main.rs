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
    
    part1(&input_data);
    part2(&input_data);
}

fn num_record_breaks(time: usize, distance: usize) -> usize {
    let mut total = 0;
    for i in 1..time{
        if i * (time - i) > distance{
            total += 1;
        }
    }
    total
}

fn part1(lines: &Vec<String>){
    let mut total = 1;
    let times: Vec<_> = lines[0].split_whitespace().collect();
    let distances: Vec<_> = lines[1].split_whitespace().collect();
    for i in 1..times.len() {
        total *= num_record_breaks(times[i].parse().expect("something"), distances[i].parse().expect("something"));
    }
    println!("{}", total)
}
fn part2(lines: &Vec<String>){
    let time: usize = lines[0].replace("Time:", "").replace(" ", "").parse().expect("something");
    let distance: usize = lines[1].replace("Distance:", "").replace(" ", "").parse().expect("something");
    let p2_ans = num_record_breaks(time, distance);
    println!("{}", p2_ans);
}