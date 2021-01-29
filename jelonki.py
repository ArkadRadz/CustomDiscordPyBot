import random
import users
import re
import discord
import messages
import setup
import datetime

symbols = ["r", "g", "b", "r2", "g2", "b2", "j"]


def print_field(field):
    for x in range(len(field)):
        for y in range(len(field[x])):
            print(field[x][y], end="")
        print()


def generate():
    return symbols[random.randint(0, 6)]


def print_discord_field(field):
    emoji_symbols = setup.return_emoji_symbols()

    final_text = ""
    for x in range(len(field)):
        for y in range(len(field[x])):
            final_text += " " + str(emoji_symbols[field[x][y]]) + " "
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
    # user_cash = int(users.read_user_data(target_user_id)) / 100
    user_data = users.read_user_data(target_user_id)
    user_cash = int(user_data['cash']) / 100

    return str(user_cash)


def create_cash_embed(payload=None, user_id=None, user_name=None, user_avatar_url=None):
    react1 = "React with ♻ to check your account balance"
    react2 = "React with 🥉 to spin for 0.50 zł"
    react3 = "React with 🥈 to spin for 1zł"
    react4 = "React with 🥇 to spin for 5zł"
    react5 = "Turn music on with 🔊 or off with 🔇"
    react_msg = react1 + "\n" + react2 + "\n" + react3 + "\n" + react4 + "\n" + react5

    if user_name is not None and user_avatar_url is not None and user_id is not None:
        embed_msg = discord.embeds.Embed(
            title="Twoje hajsy to: " + get_printable_user_cash(user_id) + " zł",
            description=react_msg,
        )
        embed_msg.set_author(name=user_name)
        embed_msg.set_thumbnail(url=user_avatar_url)
    else:
        embed_msg = discord.embeds.Embed(
            title="Twoje hajsy to: " + get_printable_user_cash(payload.user_id) + " zł",
            description=react_msg,
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
    # current_hajs = int(users.read_user_data(user_id_number))
    user_data = users.read_user_data(user_id_number)
    current_hajs = int(user_data["cash"])
    new_hajs = current_hajs + hajs_int
    users.write_user_data(user_id_number, {"cash": new_hajs})

    await message.channel.send("<@!{}> dostałeś {} groszy!".format(user_id_number, str(hajs_int)))


async def add_daily_cash(message):
    user_id_number = str(message.author.id)
    hajs_int = 100

    user_data = users.read_user_data(user_id_number)
    next_date = str(datetime.date.today() + datetime.timedelta(days=1))

    if user_data["last_daily"] == str(datetime.date.today()):
        await message.channel.send("<@!{}> oj nie nie byczku! Wróć {} po wincyj szekli.".format(user_id_number, next_date))
        return

    current_hajs = int(user_data["cash"])
    new_hajs = current_hajs + hajs_int
    users.write_user_data(user_id_number, {"cash": new_hajs, "last_daily": str(datetime.date.today())})

    await message.channel.send("<@!{}> gotowe! Wróć {} po wincyj szekli.".format(user_id_number, next_date))


async def print_user_cash(client, message):
    if client.last_hajs_message_id != 0:
        last_hajs_message = await message.channel.fetch_message(client.last_hajs_message_id)
        await message.channel.delete_messages([last_hajs_message])

    new_message = await message.channel.send(embed=create_cash_embed(
        user_name=message.author.name, user_avatar_url=message.author.avatar_url, user_id=message.author.id
    ))
    client.last_hajs_message_id = new_message.id
    await messages.add_reactions(new_message)


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
        await messages.add_reactions(message)
