from dataclasses import dataclass
from typing import List


with open("input.txt", "r") as f:
    lines = f.readlines()

@dataclass
class Reveal:
    red_count: int
    blue_count: int
    green_count: int

@dataclass
class Game:
    id: int
    reveals: List[Reveal]

possible_game_ids = set()


def parse_reveal(reveal: str) -> Reveal:
    cube_colors = reveal.split(",")
    red_count = 0
    blue_count = 0
    green_count = 0
    for cube_color in cube_colors:
        if "red" in cube_color:
            red_count = int(cube_color.replace("red", ""))
        if "blue" in cube_color:
            blue_count = int(cube_color.replace("blue", ""))
        if "green" in cube_color:
            green_count = int(cube_color.replace("green", ""))
    return Reveal(red_count, blue_count, green_count)

def parse_game(line: str) -> Game:
    reveals = line.split(";")
    beginning = reveals[0].split(":")
    game_id = int(beginning[0].replace("Game ", ""))
    print(f"Game ID: {game_id}")
    reveals[0] = beginning[1]
    print(f"Reveals: {reveals}")

    parsed_reveals: List[Reveal] = list()
    for reveal in reveals:
        parsed_reveals.append(parse_reveal(reveal))
    
    return Game(game_id, parsed_reveals)

def game_is_possible(game: Game) -> bool:
    red_available = 12
    green_available = 13
    blue_available = 14

    for reveal in game.reveals:
        if reveal.red_count > red_available or reveal.green_count > green_available or reveal.blue_count > blue_available:
            return False
        
    return True

for line in lines:
    game = parse_game(line)
    if game_is_possible(game):
        possible_game_ids.add(game.id)

print(f"Total: {sum(possible_game_ids)}")

