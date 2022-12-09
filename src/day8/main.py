from typing import List


def one(tree_map: List[List[int]]) -> int:
    rows = len(tree_map)
    cols = len(tree_map[0])
    edge_trees = rows * 2 + (cols - 2) * 2
    visbile_trees = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            vu = vd = vl = vr = True
            cl = c - 1
            cr = c + 1
            ru = r - 1
            rd = r + 1
            while cl >= 0:
                if tree_map[r][c] <= tree_map[r][cl]:
                    vl = False
                    break
                cl -= 1
            while cr <= rows - 1:
                if tree_map[r][c] <= tree_map[r][cr]:
                    vr = False
                    break
                cr += 1
            while ru >= 0:
                if tree_map[r][c] <= tree_map[ru][c]:
                    vu = False
                    break
                ru -= 1
            while rd <= cols - 1:
                if tree_map[r][c] <= tree_map[rd][c]:
                    vd = False
                    break
                rd += 1
            if any([vu, vd, vl, vr]):
                visbile_trees += 1

    return visbile_trees + edge_trees


def two(tree_map: List[List[int]]) -> int:
    rows = len(tree_map)
    cols = len(tree_map[0])
    max_visibility = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            cl = c - 1
            clc = 0
            cr = c + 1
            crc = 0
            ru = r - 1
            ruc = 0
            rd = r + 1
            rdc = 0
            while cl >= 0:
                if tree_map[r][c] <= tree_map[r][cl]:
                    clc += 1
                    break
                cl -= 1
                clc += 1
            while cr <= rows - 1:
                if tree_map[r][c] <= tree_map[r][cr]:
                    crc += 1
                    break
                cr += 1
                crc += 1
            while ru >= 0:
                if tree_map[r][c] <= tree_map[ru][c]:
                    ruc += 1
                    break
                ru -= 1
                ruc += 1
            while rd <= cols - 1:
                if tree_map[r][c] <= tree_map[rd][c]:
                    rdc += 1
                    break
                rd += 1
                rdc += 1
            current_visibility = clc * crc * ruc * rdc
            if current_visibility > max_visibility:
                max_visibility = current_visibility

    return max_visibility


if __name__ == "__main__":
    tree_map = [list(map(int, x)) for x in map(list, open("src/day8/input").read().split("\n"))]
    print(one(tree_map))
    print(two(tree_map))

