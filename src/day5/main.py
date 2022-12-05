from typing import List
from copy import deepcopy


def perform_move_one(configuration: List[List[str]], move_count: int, move_from: int, move_to: int):
    for i in range(0, move_count):
        configuration[move_to - 1].insert(0, configuration[move_from - 1].pop(0))


def perform_move_two(configuration: List[List[str]], move_count: int, move_from: int, move_to: int):
    to_append = [configuration[move_from - 1].pop(0) for _ in range(0, move_count)]

    for item in reversed(to_append):
        configuration[move_to - 1].insert(0, item)


def one(configuration: List[List[str]], actions: List[str]) -> str:
    for action in actions:
        action = action.split(" ")
        move_count, move_from, move_to = (action[1], action[3], action[5])
        perform_move_one(configuration, int(move_count), int(move_from), int(move_to))

    return ''.join([x[0] for x in configuration])


def two(configuration: List[List[str]], actions: List[str]) -> str:
    for action in actions:
        action = action.split(" ")
        move_count, move_from, move_to = (action[1], action[3], action[5])
        perform_move_two(configuration, int(move_count), int(move_from), int(move_to))

    return ''.join([x[0] for x in configuration])


def read_configuration(initial_config: str) -> List[List[str]]:
    lines = initial_config.split("\n")
    stacks = lines.pop()
    stacks = stacks.lstrip()
    stacks = stacks.rstrip()
    stacks = stacks.split("   ")
    stacks_count = max(map(int, stacks))

    final_config = []
    for i in range(0, stacks_count):
        final_config.append([])

    for line in lines:
        for i in range(0, len(line), 4):
            if line[i] == "[":
                final_config[int(i / 4)].append(line[i+1])

    return final_config


if __name__ == "__main__":

    problem_input = open("src/day5/input").read()
    str_configuration, str_actions = problem_input.split("\n\n")
    initial_configuration = read_configuration(str_configuration)
    actions_list = str_actions.split("\n")

    print(one(deepcopy(initial_configuration), actions_list))
    print(two(deepcopy(initial_configuration), actions_list))

