from typing import List


class Monkey:
    def __init__(
        self,
        id: int,
        items: List[int],
        worry_operation: str,
        worry_value: str,
        test_value: int,
        true_case: int,
        false_case: int,
    ):
        self.id = id
        self.items = items
        self.worry_operation = worry_operation
        self.worry_value = worry_value
        self.test_value = test_value
        self.true_case = true_case
        self.false_case = false_case
        self.inspected = 0
        self.determine_new_worry_level_calculation()
        self.same_next_monkey = False
        self.group_test_value = 1

    def determine_new_worry_level_calculation(self):
        if self.worry_operation == "+":
            self.get_new_worry_level = self.add_worry_level
        elif self.worry_operation == "-":
            self.get_new_worry_level = self.subtract_worry_level
        elif self.worry_operation == "*":
            self.get_new_worry_level = self.multiply_worry_level
        elif self.worry_operation == "/":
            self.get_new_worry_level = self.divide_worry_level

    def add_worry_level(self, current_level: int) -> int:
        if self.worry_value == "old":
            return current_level + current_level
        return current_level + int(self.worry_value)

    def subtract_worry_level(self, current_level: int) -> int:
        if self.worry_value == "old":
            return current_level - current_level
        return current_level - int(self.worry_value)

    def multiply_worry_level(self, current_level: int) -> int:
        if current_level == 0:
            return current_level
        if self.worry_value == "old":
            value = current_level * current_level
            return value % self.group_test_value
        value = current_level * int(self.worry_value)
        return value % self.group_test_value

    def divide_worry_level(self, current_level: int) -> int:
        if self.worry_value == "old":
            return current_level / current_level
        return current_level / int(self.worry_value)

    def __str__(self) -> str:
        return f"""
        Monkey {self.id}:
            Starting items: {self.items}
            Operation: new = old {self.worry_operation} {self.worry_value}
            Test: divisible by {self.test_value}
                If true: throw to monkey {self.true_case}
                If false: throw to monkey {self.false_case}
        """

    def calculate_new_worry_level(self, current_level: int):
        return self.get_new_worry_level(current_level)

    def run_test(self, current_level: int):
        if current_level % self.test_value == 0:
            return True
        else:
            return False
