import random

symbols = ["r", "g", "b", "r2", "g2", "b2", "j"]

def print_field(field):
    for x in range(len(field)):
        for y in range(len(field[x])):
            print(field[x][y], end="")
        print()

def generate():
    return symbols[random.randint(0, 6)]

def print_discord_field(field):
    final_text = ""
    for x in range(len(field)):
        for y in range(len(field[x])):
            final_text += " " + field[x][y] + " "
        final_text += "\n"

    return final_text

def randomize_field(field):
    for x in range(len(field)):
        for y in range(len(field[x])):
            rand = random.randint(0, 6)
            field[x][y] = symbols[rand]
    return field

def generate_field():
    return [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

def regenerate_fields(field, w):
    for x in range(len(field)):
        for y in range(len(field[x])):
            if w[x][y]:
                field[x][y] = generate()

    return field