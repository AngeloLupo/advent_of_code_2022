use std::fs;

pub fn base() -> Vec<i32> {
    let input = fs::read_to_string("src/day1/input").expect("Unable to read file");
    let elves: Vec<&str> = input.split("\n\n").collect();

    let mut calories_sums: Vec<i32> = vec![];

    for elf in elves {
        // println!("{:?}", elf);
        let tmp: Vec<i32> = elf.split("\n").map(|x| x.parse::<i32>().unwrap()).collect();
        calories_sums.push(tmp.iter().sum::<i32>());
    }
    calories_sums.sort();
    calories_sums
}

pub fn one() -> i32 {
    let mut calories_sums = base();
    calories_sums.pop().unwrap()
}

pub fn two() -> i32 {
    let mut calories_sums = base();
    calories_sums.pop().unwrap() + calories_sums.pop().unwrap() + calories_sums.pop().unwrap()
}