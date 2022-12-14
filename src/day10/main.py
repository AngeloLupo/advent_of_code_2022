from typing import List


def run(instructions: List[str]) -> (int, List[str]):
    # can't be bothered to check if everything has finished execution after we've gone trough all instructions
    instructions.append("noop")
    instructions.append("noop")

    # starting register value
    x = 1
    # starting cycle counter at 0 instead of one so I can increase it at the start of the loop
    cycle_counter = 0
    # some place to store "interesting" values
    signal_strength = []
    # dumb way of keeping track of what needs adding
    to_sum = None

    # our CRT screen
    screen = []

    # to keep track of what instructions we need to process next
    instruction_counter = 0

    # do we need to add or pick up another instruction next?
    running_instruction = False

    while True:
        cycle_counter += 1

        # keep track of "interesting" values
        if cycle_counter == 20 or ((cycle_counter - 20) % 40) == 0:
            signal_strength.append(cycle_counter * x)

        # new line on our screen
        if (cycle_counter - 1) % 40 == 0:
            screen.append([])

        # I could keep track of this when I add but that's better and we don't like better
        sprite_position = [x - 1, x, x + 1]
        # to print
        if (cycle_counter - 1) % 40 in sprite_position:
            screen[-1].append("#")
        # or not to print?
        else:
            screen[-1].append(".")

        if not running_instruction:
            # pick up new instruction or end the loop
            try:
                instruction = instructions[instruction_counter]
            except IndexError:
                break

            instruction_counter += 1

            if instruction[0] == "n":
                # noop does NO OPeration who whould have guessed
                continue
            else:
                # addx does something but in the next cycle
                running_instruction = True
                instruction = instruction.split(" ")
                to_sum = int(instruction[1])
        else:
            # addx does something in this cycle
            x += to_sum
            to_sum = None
            running_instruction = False

    # make our screen values pretty
    screen = [''.join(x) for x in screen]
    return sum(signal_strength), screen


if __name__ == "__main__":

    instructions = open("src/day10/input").read().split("\n")
    signal_strength, screen = run(instructions)
    # one
    print(signal_strength)
    # two
    [print(x) for x in screen]
