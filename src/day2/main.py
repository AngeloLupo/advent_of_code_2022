from typing import List

scores = {
    "R": 1,
    "P": 2,
    "S": 3,
    "WIN": 6,
    "DRAW": 3,
}
losses = ["RS", "SP", "PR"]
wins = ["SR", "PS", "RP"]
# Y = Draw
# Z = Win
# X = Loss
beats = {
    "R": "P",
    "P": "S",
    "S": "R"
}
is_beaten = {
    "R": "S",
    "P": "R",
    "S": "P"
}

def one(rounds: List[str]):

    score = 0

    for round in rounds:
        score += scores[round[1]]
        if round in wins:
            score += scores["WIN"]
        elif round[0] == round[1]:
            score += scores["DRAW"]
    return score


def two(rounds: List[str]):
    new_rounds = []
    for round in rounds:
        if round[1] == "Y":
            new_rounds.append(f"{round[0]}{round[0]}")
        elif round[1] == "Z":
            new_rounds.append(f"{round[0]}{beats[round[0]]}")
        else:
            new_rounds.append(f"{round[0]}{is_beaten[round[0]]}")
    return one(new_rounds)


if __name__ == "__main__":

    problem_input = open("src/day2/input").read()
    problem_input = problem_input.replace("A", "R")
    problem_input = problem_input.replace("B", "P")
    problem_input = problem_input.replace("C", "S")
    problem_input_1 = problem_input.replace("Y", "P")
    problem_input_1 = problem_input_1.replace("X", "R")
    problem_input_1 = problem_input_1.replace("Z", "S")

    rounds_1 = problem_input_1.replace(" ", "")
    rounds_1 = rounds_1.split("\n")

    rounds_2 = problem_input.replace(" ", "")
    rounds_2 = rounds_2.split("\n")

    print(one(rounds_1))
    print(two(rounds_2))

