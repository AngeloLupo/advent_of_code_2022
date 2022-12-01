def compute_calories(problem_input: str):
    elfs = problem_input.split("\n\n")
    calories_sums = []

    for elf in elfs:
        elf = elf.split("\n")
        calories = 0
        for snack in elf:
            calories += int(snack)
        calories_sums.append(calories)
    return sorted(calories_sums)


def one(calories_sums: list):
    return calories_sums[-1]


def two(calories_sums: list):
    return calories_sums[-1] + calories_sums[-2] + calories_sums[-3]


if __name__ == "__main__":
    problem_input = open("1/input").read()
    calories_sum = compute_calories(problem_input)

    print(one(calories_sum))
    print(two(calories_sum))

