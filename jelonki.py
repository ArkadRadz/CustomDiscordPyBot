import random
import users
import re
import discord

symbols = ["r", "g", "b", "r2", "g2", "b2", "j"]

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

emoji_symbols = {
    "r" : ":red_circle:",
    "g" : ":green_circle:",
    "b" : ":blue_circle:",
    "r2": ":japanese_goblin:",
    "g2": ":leafy_green:",
    "b2": ":blueberries:",
    "d3": ":lemon:",
    "d4": ":lemon:",
    "d5": ":lemon:",
    "j" : ":deer:"
}

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
            final_text += " " + emoji_symbols[field[x][y]] + " "
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


def get_printable_user_cash(target_user_id):
    user_cash = int(users.read_user_data(target_user_id)) / 100

    return str(user_cash)

def create_cash_embed(payload = None, user_id = None, user_name = None, user_avatar_url = None):
    if user_name is not None and user_avatar_url is not None and user_id is not None:
        embed_msg = discord.embeds.Embed(
            title="Twoje hajsy to: " + get_printable_user_cash(user_id) + " zł",
            description="TODO",
        )
        embed_msg.set_author(name=user_name)
        embed_msg.set_thumbnail(url=user_avatar_url)
    else:
        embed_msg = discord.embeds.Embed(
            title="Twoje hajsy to: " + get_printable_user_cash(payload.user_id) + " zł",
            description="TODO",
        )
        embed_msg.set_author(name=payload.member.name)
        embed_msg.set_thumbnail(url=payload.member.avatar_url)

    return embed_msg

async def add_cash(message):
    user_id = re.search("<@!\d+>", message.content)

    if None == user_id:
        user_id = re.search("<@\d+>", message.content)

    hajs = re.search("\d+gr", message.content)
    if None == user_id or None == hajs:
        await message.channel.send(
            'HALO POLICJA OSZUKUJO, NIE PODAJO UŻYTKOWNIKA [@uzytkownik] ANI/LUB HAJSU [liczba naturalna z końcówką gr np. 100gr]')
        return

    user_id_number = re.search("\d+", user_id.group()).group()
    hajs_int = int(re.search("\d+", hajs.group()).group())
    current_hajs = int(users.read_user_data(user_id_number))
    new_hajs = current_hajs + hajs_int
    users.write_user_data(user_id_number, new_hajs)

    await message.channel.send("<@!{}> dostałeś {} groszy!".format(user_id_number, str(hajs_int)))


async def print_user_cash(client, message):
    if client.last_hajs_message_id != 0:
        last_hajs_message = await message.channel.fetch_message(client.last_hajs_message_id)
        await message.channel.delete_messages([last_hajs_message])

    new_message = await message.channel.send(embed=create_cash_embed(
        user_name=message.author.name, user_avatar_url=message.author.avatar_url, user_id=message.author.id
    ))
    client.last_hajs_message_id = new_message.id
    await new_message.add_reaction('♻')


async def update_user_cash_message(
        payload=None, user_id=None, user_name=None, user_avatar_url=None, message=None):
    await message.clear_reactions()
    edited_embed = None
    if payload is not None:
        edited_embed = create_cash_embed(payload=payload)

    if user_name is not None and user_avatar_url is not None and user_id is not None:
        edited_embed = create_cash_embed(user_name=user_name, user_avatar_url=user_avatar_url, user_id=user_id)

    if edited_embed is not None:
        await message.edit(embed=edited_embed)
        await message.add_reaction('♻')
