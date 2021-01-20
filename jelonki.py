import random

symbols = ["🦌", "🐂", "🐒", "🧸", "🐕"]

def print_field(field):
    for x in range(len(field)):
        for y in range(len(field[x])):
            print(field[x][y], end="")
        print()

def print_discord_field(field):
    final_text = ""
    for x in range(len(field)):
        for y in range(len(field[x])):
            final_text += " " + symbols[field[x][y]] + " "
        final_text += "\n"

    return final_text

def randomize_field(field):
    for x in range(len(field)):
        for y in range(len(field[x])):
            field[x][y] = random.randint(0, 4)
    return field

def generate_field():
    return [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
