import utils
import json

setup_dir = "setup"

emoji_symbols = {
    "r": None,
    "g": None,
    "b": None,
    "r2": None,
    "g2": None,
    "b2": None,
    "d3": None,
    "d4": None,
    "d5": None,
    "j": None
}


def return_emoji_symbols():
    return emoji_symbols


def is_setup_finished():
    for emoji in emoji_symbols.values():
        if emoji is None:
            return False

    return True


def return_first_none_emoji():
    for emoji in emoji_symbols.keys():
        if emoji_symbols[emoji] is None:
            return emoji


def return_emoji(emoji):
    if emoji in emoji_symbols.keys():
        return emoji_symbols[emoji]

def set_emoji_symbol(emoji, new_value):
    if emoji in emoji_symbols.keys():
        emoji_symbols[emoji] = new_value


def create_configuration(server_id):
    utils.check_if_dir_exists(setup_dir)
    server_string = setup_dir + "/" + str(server_id)
    f = open(server_string, "w")
    f.write(json.dumps(emoji_symbols, ensure_ascii=False))
    f.close()

def read_configuration(server_id):
    utils.check_if_dir_exists(setup_dir)
    server_string = setup_dir + "/" + str(server_id)
    try:
        f = open(server_string, "r")
        configuration = json.load(f)
        f.close()
        return configuration
    except IOError:
        print("Configuration for server " + str(server_id) + " does not exist.")
        return None
