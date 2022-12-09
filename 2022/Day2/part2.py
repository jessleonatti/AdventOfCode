with open("input.txt", "r") as f:
    lines = f.readlines()

hand_shape_to_score = {"rock": 1, "paper": 2, "scissors": 3}

opponent = {"A": "rock", "B": "paper", "C": "scissors"}

own = {"X": "rock", "Y": "paper", "Z": "scissors"}

win = {"scissors rock", "paper scissors", "rock paper"}
tie = {"rock rock", "paper paper", "scissors scissors"}

beat = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}

lose_to = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

total = 0
for line in lines:
    line = line.replace("\n", "")

    opponent_choice, outcome = line.split(" ")
    opponent_shape = opponent[opponent_choice]

    if outcome == "Y":
        # Needs to end in a draw, so choose the same hand shape
        # as the opponent
        own_shape = opponent_shape
    elif outcome == "Z":
        # Win
        own_shape = beat[opponent_shape]
    else:
        # Lose
        own_shape = lose_to[opponent_shape]

    if line in win:
        total += 6
    elif line in tie:
        total += 3

    value = hand_shape_to_score[own_shape]
    total += value

print(f"total: {total}")
