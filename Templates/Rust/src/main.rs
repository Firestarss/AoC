use std::fs::read_to_string;
 
fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename) 
        .unwrap()  // panic on possible file-reading errors
        .lines()  // split the string into an iterator of string slices
        .map(String::from)  // make each slice into a string
        .collect()  // gather them together into a vector
}
 
fn main() {
    let input_num = 0;
    let input_paths = ["./input.txt", "./test_input.txt"];
    let input_data = read_lines(input_paths[input_num]);
    
    part1(&input_data);
    part2(&input_data);
}

part1(){}
part2(){}