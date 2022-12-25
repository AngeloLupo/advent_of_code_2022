from heapq import heappush, heappop
from typing import List, Tuple


def get_neightbors(input_map: List[List[str]], row: int, col: int):
    h = get_height(input_map, row, col)
    neighbors = []
    for dis_r, dis_c in ([-1, 0], [1, 0], [0, -1], [0, 1]):
        r1, c1 = row + dis_r, col + dis_c
        if r1 >= 0 and r1 < len(input_map) and c1 >= 0 and c1 < len(input_map[0]):
            if get_height(input_map, r1, c1) <= h + 1:
                neighbors.append((r1, c1))
    return neighbors


def get_height(input_map: List[List[str]], row: int, col: int):
    s = input_map[row][col]
    if s == "S":
        return 0
    if s == "E":
        return 25
    return ord(s) - 97


def get_steps(input_map: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    visited = set()
    prio_queue = []
    heappush(prio_queue, (0, start))

    while True:
        if not prio_queue:
            break

        steps, node = heappop(prio_queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                return steps
            for rnew, cnew in get_neightbors(input_map, node[0], node[1]):
                heappush(prio_queue, (steps+1, (rnew, cnew)))


if __name__ == "__main__":
    input_map = open("src/day12/input").read().split("\n")
    input_map = [[char for char in row] for row in input_map]

    starting_positions = []
    for row in range(len(input_map)):
        for col in range(len(input_map[0])):
            if input_map[row][col] == "S":
                starting_position = (row, col)
                starting_positions.append((row, col))
            if input_map[row][col] == "E":
                end_position = (row, col)
            if input_map[row][col] == "a":
                starting_positions.append((row, col))

    print(get_steps(input_map, starting_position, end_position))

    steps_all = []
    for position in starting_positions:
        steps = get_steps(input_map, position, end_position)
        if steps is not None:
            steps_all.append(steps)

    print(min(steps_all))


