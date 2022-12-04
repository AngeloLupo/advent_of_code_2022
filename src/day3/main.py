import string
from typing import List

priorities = f"_{string.ascii_lowercase}{string.ascii_uppercase}"


def calculate_priority(letter: str):
    return priorities.index(letter)


def get_common_items(rucksacks: List[str]) -> List[str]:
    common_items = []
    for rucksack in rucksacks:
        split_position = int(len(rucksack)/2)
        first_compartment = rucksack[0:split_position]
        second_compartment = rucksack[split_position::]
        for item in first_compartment:
            if item in second_compartment:
                common_items.append(item)
                break
    return common_items


def one(rucksacks: List[str]) -> int:
    common_items = get_common_items(rucksacks)
    return sum(map(calculate_priority, common_items))


def get_group_badges(rucksacks: List[str]):
    group_badges = []
    for i in range(0, int(len(rucksacks))-1, 3):
        for letter in rucksacks[i]:
            if letter in rucksacks[i+1] and letter in rucksacks[i+2]:
                group_badges.append(letter)
                break
    return group_badges


def two(rucksacks: List[str]) -> int:
    group_badges = get_group_badges(rucksacks)
    return sum(map(calculate_priority, group_badges))


if __name__ == "__main__":

    problem_input = open("src/day3/input").read()
    rucksacks = problem_input.split("\n")

    print(one(rucksacks))
    print(two(rucksacks))

