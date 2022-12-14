from typing import Dict


class Monkey:
    def __init__(self, descriptor: str, id: int):
        self.id = id
        descriptor = descriptor.split("\n")
        self.original_items = [int(x) for x in descriptor[1].split(":")[1].split(",")]
        self.items = [int(x) for x in descriptor[1].split(":")[1].split(",")]
        self.operation, operation_term = descriptor[2].split("=")[1].strip().split(" ")[1:]
        if operation_term == "old":
            self.operation_term = "item"
        else:
            self.operation_term = int(operation_term)
        self.test = int(descriptor[3].split(" ")[-1])
        self.true_throw = int(descriptor[4].split(" ")[-1])
        self.false_throw = int(descriptor[5].split(" ")[-1])
        self.tests = 0

    def play_round(self, monkeys: Dict[int, "Monkey"], divide: bool, tests: int = None) -> None:
        for i in range(0, len(self.items)):
            self.tests += 1
            item = self.items[i]
            item = eval(f"{item} {self.operation} {self.operation_term}")
            if tests:
                item = item % tests
            if divide:
                item = item // 3
            if item % self.test == 0:
                monkeys[self.true_throw].items.append(item)
            else:
                monkeys[self.false_throw].items.append(item)
        self.items = []

    def __repr__(self) -> str:
        return f"ID: {self.id}\n" \
               f"Items: {self.items}\n" \
               f"Operation: news = old {self.operation} {self.operation_term}\n" \
               f"Test: {self.test}\n" \
               f"\t True: {self.true_throw}\n" \
               f"\t False: {self.false_throw}\n" \
               f"Tests: {self.tests}"


if __name__ == "__main__":
    monkeys_str = open("src/day11/input").read().split("\n\n")
    monkeys = {counter: Monkey(monkey, counter) for counter, monkey in enumerate(monkeys_str)}
    for _ in range(0, 20):
        for monkey in monkeys.values():
            monkey.play_round(monkeys, True)
    monkey_businesses = sorted([monkey.tests for monkey in monkeys.values()])
    print(monkey_businesses[-1] * monkey_businesses[-2])

    for monkey in monkeys.values():
        monkey.tests = 0
        # I did not go crazy because I forgot to reset the item values, I did not
        monkey.items = monkey.original_items

    common_multiple = 1
    for x in monkeys.values():
        common_multiple *= x.test
    for _ in range(0, 10000):
        for monkey in monkeys.values():
            monkey.play_round(monkeys, False, common_multiple)
    monkey_businesses = sorted([monkey.tests for monkey in monkeys.values()])
    print(monkey_businesses[-1] * monkey_businesses[-2])
