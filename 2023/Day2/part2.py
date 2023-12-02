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

def min_game(game: Game) -> Reveal:
    min_red = -1
    min_green = -1
    min_blue = -1

    for reveal in game.reveals:
        if reveal.red_count > min_red:
            min_red = reveal.red_count
        
        if reveal.green_count > min_green:
            min_green = reveal.green_count

        if reveal.blue_count > min_blue:
            min_blue = reveal.blue_count
        
    return Reveal(min_red, min_blue, min_green)

running_min_game_reveal = 0
for line in lines:
    game = parse_game(line)
    min_game_reveal = min_game(game)
    power = min_game_reveal.blue_count*min_game_reveal.green_count*min_game_reveal.red_count
    print(f"Game {game.id} power: {power}")
    running_min_game_reveal += power

print(f"Total power: {running_min_game_reveal}")


