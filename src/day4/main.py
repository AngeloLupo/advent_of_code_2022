from typing import List


def get_ranges_pairs(assignments: List[str]) -> (List[List[str]], List[List[List[str]]]):
    ranges_pairs = []
    jranges_pairs = []
    for pairs in assignments:
        pairs = pairs.split(",")

        range_1 = pairs[0].split("-")
        range_2 = pairs[1].split("-")

        jrange_1 = [str(_) for _ in range(int(range_1[0]), int(range_1[1]) + 1)]
        jrange_2 = [str(_) for _ in range(int(range_2[0]), int(range_2[1]) + 1)]

        ranges_pairs.append([
            f"-{'-'.join(jrange_1)}-",
            f"-{'-'.join(jrange_2)}-",
        ])
        jranges_pairs.append([jrange_1, jrange_2])

    return ranges_pairs, jranges_pairs


def one(ranges_pairs: List[List[str]]) -> int:
    contained_ranges = 0
    for x, y in ranges_pairs:
        if x in y or y in x:
            contained_ranges += 1
    return contained_ranges


def two(jranges_pairs: List[List[List[str]]]) -> int:
    overlapping_pairs = 0
    for p1, p2 in jranges_pairs:
        if (
            p1[0] in p2 or p1[-1] in p2
        ) or (
            p2[0] in p1 or p2[-1] in p1
        ):
            overlapping_pairs += 1
    return overlapping_pairs


if __name__ == "__main__":

    problem_input = open("src/day4/input").read()
    assignments = problem_input.split("\n")

    ranges_pairs, jranges_pairs = get_ranges_pairs(assignments)

    print(one(ranges_pairs))
    print(two(jranges_pairs))

