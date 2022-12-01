use std::io::{stdin,stdout,Write};

mod day1;
// mod day2;
// mod day3;
// mod day4;
// mod day5;
// mod day6;
// mod day7;
// mod day8;
// mod day9;
// mod day10;
// mod day11;

fn main() {

    let mut s=String::new();
    print!("Please enter some text: ");
    let _=stdout().flush();
    stdin().read_line(&mut s).expect("Did not enter a correct string");
    if let Some('\n')=s.chars().next_back() {
        s.pop();
    }
    if let Some('\r')=s.chars().next_back() {
        s.pop();
    }

    match s.as_str() {
        "1" => { println!("day1_1: {}", day1::one()); println!("day1_2: {}", day1::two()); }
        // "2" => { println!("day2_1: {}", day2::one()); println!("day2_2: {}", day2::two()); }
        // "3" => { println!("day3_1: {}", day3::one(3, 1)); println!("day3_2: {}", day3::two()); }
        // "4" => { println!("day4_1: {}", day4::one()); println!("day4_2: {}", day4::two()); }
        // "5" => { println!("day5_1: {}", day5::one()); println!("day5_2: {}", day5::two()); }
        // "6" => { println!("day6_1: {}", day6::one()); println!("day6_2: {}", day6::two()); }
        // "7" => { println!("day7_1: {}", day7::one()); println!("day7_2: {}", day7::two()); }
        // "8" => { println!("day8_1: {}", day8::one(0).1); println!("day8_2: {}", day8::two()); }
        // "9" => { println!("day9_1: {}", day9::one()); println!("day9_2: {}", day9::two()); }
        // "10" => { println!("day10_1: {}", day10::one()); println!("day10_2: {}", day10::two()); }
        // "11" => { println!("day11_1: {}", day11::one()); println!("day11_2: {}", day11::two()); }
         _ => println!("Invalid selection: {}", s)
    }
}