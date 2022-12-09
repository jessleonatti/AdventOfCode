with open("input.txt", "r") as f:
    lines = f.readlines()

opponent_strategy_to_score = {"rock": 1, "paper": 2, "scissors": 3}

own_strategy_to_score = {"rock": 1, "paper": 2, "scissors": 3}

opponent = {"A": "rock", "B": "paper", "C": "scissors"}

own = {"X": "rock", "Y": "paper", "Z": "scissors"}

win = {"scissors rock", "paper scissors", "rock paper"}
tie = {"rock rock", "paper paper", "scissors scissors"}

total = 0
for line in lines:
    line = line.replace("\n", "")

    opponent_choice, own_choice = line.split(" ")
    opponent_shape = opponent[opponent_choice]

    own_shape = own[own_choice]

    line = f"{opponent_shape} {own_shape}"
    if line in win:
        total += 6

    elif line in tie:
        total += 3

    value = own_strategy_to_score[own_shape]
    total += value

print(f"total: {total}")
