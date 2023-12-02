import math
from typing import List
from monkey import Monkey

def parse_monkeys(monkey_notes):
    monkeys: List[Monkey] = []
    for i, monkey_note in enumerate(monkey_notes):
        monkey_parts = monkey_note.split("\n ")

        # Starting items
        starting_items = monkey_parts[1].replace(" Starting items: ", "")
        starting_items = [int(item) for item in starting_items.split(", ")]

        # Operation
        operation = monkey_parts[2].replace(" Operation: new = old ", "")
        operation = operation.split(" ")
        worry_operation = operation[0]
        worry_value = operation[1]

        # Test
        test = monkey_parts[3].replace(" Test: divisible by ", "")
        test_value = int(test)

        # True case
        true_case = monkey_parts[4].replace("  If true: throw to monkey ", "")
        true_case = int(true_case)

        # False case
        false_case = monkey_parts[5].replace("  If false: throw to monkey ", "")
        false_case = int(false_case)

        monkey = Monkey(
            i, 
            starting_items,
            worry_operation,
            worry_value,
            test_value,
            true_case,
            false_case,
        )
        monkeys.append(monkey)
    return monkeys

def go_through_items(monkey: Monkey, monkeys: List[Monkey]):
    for _ in range(len(monkey.items)):
        item = monkey.items.pop(0)
        monkey.inspected += 1

        item = monkey.get_new_worry_level(item)

        item = math.floor(int(item) / 3)
        test_result = monkey.run_test(item)
        next_monkey = monkey.true_case if test_result else monkey.false_case
        throw_to_monkey(item, monkeys, next_monkey)
    return monkey

def throw_to_monkey(item: int, monkeys: List[Monkey], monkey_index: int):
    monkeys[monkey_index].items.append(item)

def main():
    with open("input.txt", "r") as f:
        monkey_notes = f.read()

    monkey_notes = monkey_notes.split("\n\n")
    monkeys = parse_monkeys(monkey_notes)
    
    # Go through 20 rounds
    for i in range(20):
        # Each monkey gets a turn
        for j, monkey in enumerate(monkeys):
            monkey = go_through_items(monkey, monkeys)
            monkeys[j] = monkey
    for monkey in monkeys:
        print(f"Monkey {monkey.id} inspected items {monkey.inspected} times.")


if __name__ == "__main__":
    main()
