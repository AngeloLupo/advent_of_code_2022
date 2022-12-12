from typing import List, Set
from dataclasses import dataclass


@dataclass
class Rope:
    hx: int = 0
    hy: int = 0
    tx: int = 0
    ty: int = 0
    head_visited_coordinates: List[str] = None
    tail_visited_coordinates: List[str] = None

    def __post_init__(self):
        self.head_visited_coordinates = ["0:0"]
        self.tail_visited_coordinates = ["0:0"]

    def get_coordinates(self, knot: str = "head") -> str:
        if knot == "tail":
            return f"{self.tx}:{self.ty}"
        return f"{self.hx}:{self.hy}"

    def tail_needs_moving(self) -> bool:
        if self.tx == self.hx:
            if abs(self.ty - self.hy) in [0, 1]:
                return False
        if self.ty == self.hy:
            if abs(self.tx - self.hx) in [0, 1]:
                return False
        return True

    def _move_head(self, direction: str):
            if direction == "U":
                self.hx += 1
            if direction == "D":
                self.hx -= 1
            if direction == "R":
                self.hy += 1
            if direction == "L":
                self.hy -= 1

    def _move_tail(self, direction: str):
        if self.hx != self.tx and self.hy != self.ty:
            if self.hx - self.tx == 2:
                self.tx = self.hx - 1
                self.ty = self.hy
            if self.hx - self.tx == -2:
                self.tx = self.hx + 1
                self.ty = self.hy
            if self.hy - self.ty == 2:
                self.ty = self.hy - 1
                self.tx = self.hx
            if self.hy - self.ty == -2:
                self.ty = self.hy + 1
                self.tx = self.hx
        else:
            if direction == "U":
                self.tx += 1
            if direction == "D":
                self.tx -= 1
            if direction == "R":
                self.ty += 1
            if direction == "L":
                self.ty -= 1

    def move(self, direction: str, count: int):
        for _ in range(0, count):
            self._move_head(direction)
            self.head_visited_coordinates.append(self.get_coordinates())
            if self.tail_needs_moving():
                self._move_tail(direction)
                self.tail_visited_coordinates.append(self.get_coordinates("tail"))

    def unique_head_coordinates_count(self) -> int:
        return len(set(self.head_visited_coordinates))

    def unique_tail_coordinates_count(self) -> int:
        return len(set(self.tail_visited_coordinates))


def one(comands: List[str]) -> int:
    rope = Rope()
    for comand in comands:
        comand = comand.split(" ")
        rope.move(comand[0], int(comand[1]))
    return rope.unique_tail_coordinates_count()


if __name__ == "__main__":
    comands = open("src/day9/input").read().split("\n")
    print(one(comands))
