from typing import List, Set, Optional
from dataclasses import dataclass


@dataclass
class Rope:
    id: int
    following: Optional["Rope"]
    x: int = 0
    y: int = 0
    visited_coordinates: List[str] = None

    def __repr__(self):
        string = f"Rope {self.id}"
        if self.following:
            return f"{string} following {self.following.id}"
        return string

    def __post_init__(self):
        self.visited_coordinates = ["0:0"]

    def get_coordinates(self) -> str:
        return f"{self.x}:{self.y}"

    def _move(self, direction: str):
            if direction == "U":
                self.x += 1
            if direction == "D":
                self.x -= 1
            if direction == "R":
                self.y += 1
            if direction == "L":
                self.y -= 1

    def _move_with_following(self):
        delta_x = self.following.x - self.x
        delta_y = self.following.y - self.y
        if abs(delta_x) <= 1 and abs(delta_y) <= 1:
            return
        if abs(delta_x) < abs(delta_y):
            self.x = self.following.x
            self.y = self.following.y - delta_y // abs(delta_y)
        elif abs(delta_x) > abs(delta_y):
            self.x = self.following.x - delta_x // abs(delta_x)
            self.y = self.following.y
        else:
            self.x = self.following.x - delta_x // abs(delta_x)
            self.y = self.following.y - delta_y // abs(delta_y)

    def needs_moving(self) -> bool:
        if self.following.x == self.x:
            if abs(self.following.y - self.y) in [0, 1]:
                return False
        if self.following.y == self.y:
            if abs(self.following.x - self.x) in [0, 1]:
                return False
        return True

    def move(self, direction: str):
        if self.following:
            if self.needs_moving():
                self._move_with_following()
        else:
            self._move(direction)
        self.visited_coordinates.append(self.get_coordinates())

    def unique_coordinates_count(self) -> int:
        return len(set(self.visited_coordinates))


def init_ropes() -> List[Rope]:
    ropes = []
    prev = None
    for i in range(0, 10):
        rope = Rope(following=prev, id=i)
        prev = rope
        ropes.append(rope)
    return ropes


def two(comands: List[str]) -> int:
    ropes = init_ropes()
    for comand in comands:
        comand = comand.split(" ")
        for i in range(0, int(comand[1])):
            for rope in ropes:
                rope.move(comand[0])
    return ropes[-1].unique_coordinates_count()


if __name__ == "__main__":
    comands = open("src/day9/input").read().split("\n")
    print(two(comands))
