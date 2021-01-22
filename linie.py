import jelonki
import asyncio
import users
import re


def check(b, t, w, respin_board):
    d3 = {"r": 0.2, "g": 0.2, "b": 0.2, "r2": 1, "g2": 0.5, "b2": 0.5, "j": 2}
    d4 = {"r": 0.5, "g": 0.5, "b": 0.5, "r2": 2, "g2": 1, "b2": 1, "j": 6}
    d5 = {"r": 2, "g": 1.5, "b": 1, "r2": 10, "g2": 5, "b2": 4, "j": 40}

    total = 0
    sum = 0
    last_sum = 0
    spin = True
    if w[0][2]:
        if t[0][0] == t[0][1] == t[0][2] == t[0][3] == t[0][4]:
            sum += b * d5[t[0][0]]
            w[0][2] = False
            w[0][1] = False
            w[0][0] = False
            respin_board[0][0], respin_board[0][1], respin_board[0][2], respin_board[0][3], respin_board[0][
                4] = False, False, False, False, False
    if w[0][1]:
        if t[0][0] == t[0][1] == t[0][2] == t[0][3]:
            sum += b * d4[t[0][0]]
            w[0][1] = False
            w[0][0] = False
            respin_board[0][0], respin_board[0][1], respin_board[0][2], respin_board[0][3] = False, False, False, False
    if w[0][0]:
        if t[0][0] == t[0][1] == t[0][2]:
            sum += b * d3[t[0][0]]
            w[0][0] = False
            respin_board[0][0], respin_board[0][1], respin_board[0][2] = False, False, False

    if w[0][5]:
        if t[1][0] == t[1][1] == t[1][2] == t[1][3] == t[1][4]:
            sum += b * d5[t[1][0]]
            w[0][5] = False
            w[0][4] = False
            w[0][3] = False
            respin_board[1][0], respin_board[1][1], respin_board[1][2], respin_board[1][3], respin_board[1][
                4] = False, False, False, False, False
    if w[0][4]:
        if t[1][0] == t[1][1] == t[1][2] == t[1][3]:
            sum += b * d4[t[1][0]]
            w[0][4] = False
            w[0][3] = False
            respin_board[1][0], respin_board[1][1], respin_board[1][2], respin_board[1][3] = False, False, False, False
    if w[0][3]:
        if t[1][0] == t[1][1] == t[1][2]:
            sum += b * d3[t[1][0]]
            w[0][3] = False
            respin_board[1][0], respin_board[1][1], respin_board[1][2] = False, False, False

    if w[0][8]:
        if t[2][0] == t[2][1] == t[2][2] == t[2][3] == t[2][4]:
            sum += b * d5[t[2][0]]
            w[0][8] = False
            w[0][7] = False
            w[0][6] = False
            respin_board[2][0], respin_board[2][1], respin_board[2][2], respin_board[2][3], respin_board[2][
                4] = False, False, False, False, False
    if w[0][7]:
        if t[2][0] == t[2][1] == t[2][2] == t[2][3]:
            sum += b * d4[t[2][0]]
            w[0][7] = False
            w[0][6] = False
            respin_board[2][0], respin_board[2][1], respin_board[2][2], respin_board[2][3] = False, False, False, False
    if w[0][6]:
        if t[2][0] == t[2][1] == t[2][2]:
            sum += b * d3[t[2][0]]
            w[0][6] = False
            respin_board[2][0], respin_board[2][1], respin_board[2][2] = False, False, False

    if w[1][2]:
        if t[0][0] == t[1][1] == t[2][2] == t[1][3] == t[0][4]:
            sum += b * d5[t[0][0]]
            w[1][2] = False
            w[1][1] = False
            w[1][0] = False
            respin_board[0][0], respin_board[1][1], respin_board[2][2], respin_board[1][3], respin_board[0][
                4] = False, False, False, False, False
    if w[1][1]:
        if t[0][0] == t[1][1] == t[2][2] == t[1][3]:
            sum += b * d4[t[0][0]]
            w[1][1] = False
            w[1][0] = False
            respin_board[0][0], respin_board[1][1], respin_board[2][2], respin_board[1][3] = False, False, False, False
    if w[1][0]:
        if t[0][0] == t[1][1] == t[2][2]:
            sum += b * d3[t[0][0]]
            w[1][0] = False
            respin_board[0][0], respin_board[1][1], respin_board[2][2] = False, False, False

    if w[1][5]:
        if t[2][0] == t[1][1] == t[0][2] == t[1][3] == t[2][4]:
            sum += b * d5[t[2][0]]
            w[1][5] = False
            w[1][4] = False
            w[1][3] = False
            respin_board[2][0], respin_board[1][1], respin_board[0][2], respin_board[1][3], respin_board[2][
                4] = False, False, False, False, False
    if w[1][4]:
        if t[2][0] == t[1][1] == t[0][2] == t[1][3]:
            sum += b * d4[t[2][0]]
            w[1][4] = False
            w[1][3] = False
            respin_board[2][0], respin_board[1][1], respin_board[0][2], respin_board[1][3] = False, False, False, False
    if w[1][3]:
        if t[2][0] == t[1][1] == t[0][2]:
            sum += b * d3[t[2][0]]
            w[1][3] = False
            respin_board[2][0], respin_board[1][1], respin_board[0][2] = False, False, False

    if w[1][8]:
        if t[1][0] == t[0][1] == t[0][2] == t[0][3] == t[1][4]:
            sum += b * d5[t[1][0]]
            w[1][8] = False
            w[1][7] = False
            w[1][6] = False
            respin_board[1][0], respin_board[0][1], respin_board[0][2], respin_board[0][3], respin_board[1][
                4] = False, False, False, False, False
    if w[1][7]:
        if t[1][0] == t[0][1] == t[0][2] == t[0][3]:
            sum += b * d4[t[1][0]]
            w[1][7] = False
            w[1][6] = False
            respin_board[1][0], respin_board[0][1], respin_board[0][2], respin_board[0][3] = False, False, False, False
    if w[1][6]:
        if t[1][0] == t[0][1] == t[0][2]:
            sum += b * d3[t[1][0]]
            w[1][6] = False
            respin_board[1][0], respin_board[0][1], respin_board[0][2] = False, False, False

    if w[2][2]:
        if t[1][0] == t[2][1] == t[2][2] == t[2][3] == t[1][4]:
            sum += b * d5[t[1][0]]
            w[2][2] = False
            w[2][1] = False
            w[2][0] = False
            respin_board[1][0], respin_board[2][1], respin_board[2][2], respin_board[2][3], respin_board[1][
                4] = False, False, False, False, False
    if w[2][1]:
        if t[1][0] == t[2][1] == t[2][2] == t[2][3]:
            sum += b * d4[t[1][0]]
            w[2][1] = False
            w[2][0] = False
            respin_board[1][0], respin_board[2][1], respin_board[2][2], respin_board[2][3] = False, False, False, False
    if w[2][0]:
        if t[1][0] == t[2][1] == t[2][2]:
            sum += b * d3[t[1][0]]
            w[2][0] = False
            respin_board[1][0], respin_board[2][1], respin_board[2][2] = False, False, False

    if w[2][5]:
        if t[0][0] == t[1][1] == t[1][2] == t[1][3] == t[0][4]:
            sum += b * d5[t[0][0]]
            w[2][5] = False
            w[2][4] = False
            w[2][3] = False
            respin_board[0][0], respin_board[1][1], respin_board[1][2], respin_board[1][3], respin_board[0][
                4] = False, False, False, False, False
    if w[2][4]:
        if t[0][0] == t[1][1] == t[1][2] == t[1][3]:
            sum += b * d4[t[0][0]]
            w[2][4] = False
            w[2][3] = False
            respin_board[0][0], respin_board[1][1], respin_board[1][2], respin_board[1][3] = False, False, False, False
    if w[2][3]:
        if t[0][0] == t[1][1] == t[1][2]:
            sum += b * d3[t[0][0]]
            w[2][3] = False
            respin_board[0][0], respin_board[1][1], respin_board[1][2] = False, False, False

    if w[2][8]:
        if t[2][0] == t[1][1] == t[1][2] == t[1][3] == t[2][4]:
            sum += b * d5[t[2][0]]
            w[2][8] = False
            w[2][7] = False
            w[2][6] = False
            respin_board[2][0], respin_board[1][1], respin_board[1][2], respin_board[1][3], respin_board[2][
                4] = False, False, False, False, False
    if w[2][7]:
        if t[2][0] == t[1][1] == t[1][2] == t[1][3]:
            sum += b * d4[t[2][0]]
            w[2][7] = False
            w[2][6] = False
            respin_board[2][0], respin_board[1][1], respin_board[1][2], respin_board[1][3] = False, False, False, False
    if w[2][6]:
        if t[2][0] == t[1][1] == t[1][2]:
            sum += b * d3[t[2][0]]
            w[2][6] = False
            respin_board[2][0], respin_board[1][1], respin_board[1][2] = False, False, False

    if sum > 0:
        total += sum
        spin = True
    else:
        spin = False
        total += last_sum

    return [total, w, respin_board, spin]


def isfloat(x):
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


async def modify_cash(target_id, value=None):
    user_cash = users.read_user_data(target_id)
    if value is None:
        final_cash = int(user_cash) - 50
    else:
        if isint(x=value):
            final_cash = int(user_cash) + int(value)
        else:
            cash = float(value) * 100
            final_cash = int(user_cash) + int(cash)

    if final_cash > 0:
        users.write_user_data(str(target_id), str(final_cash))
        return True
    else:
        return False


async def spin(message=None, bet=None, payload=None):
    if message is not None:
        user_name = message.author.name
        user_avatar_url = message.author.avatar_url
        user_id = message.author.id
    if payload is not None:
        user_name = payload.member.name
        user_avatar_url = payload.member.avatar_url
        user_id = payload.member.id

    if bet is not None:
        bet = re.search("\d+", bet).group()
        can_play = await modify_cash(user_id, -abs(int(bet)))
    else:
        can_play = await modify_cash(user_id, bet)

    if not can_play:
        await send_embed_msg(message, user_avatar_url, user_id, user_name, custom_text="Not enough cash!")
        return

    def create_game_board_message():
        return jelonki.print_discord_field(game_board)

    w = [[True for i in range(9)] for i in range(3)]
    respin_board = [[True for i in range(5)] for i in range(3)]

    game_board = jelonki.generate_field()
    game_board = jelonki.randomize_field(game_board)
    embed_msg = create_game_board_message()

    await message.channel.send(embed_msg)
    rezultat = check(1, game_board, w, respin_board)
    last_spin = rezultat[0]
    total = rezultat[0]
    while rezultat[3]:
        await message.channel.send("rezultat[0] == " + str(rezultat[0]))

        await asyncio.sleep(5)
        await message.channel.send(":flag_va: :flag_va: :flag_va: :flag_va: :flag_va: :flag_va: :flag_va: :flag_va: ")
        respin_board = rezultat[2]
        w = rezultat[1]
        game_board = jelonki.regenerate_fields(game_board, rezultat[2])
        last_spin = rezultat[0]
        rezultat = check(1, game_board, w, respin_board)
        total += rezultat[0]
        embed_msg = create_game_board_message()
        await message.channel.send(embed_msg)

    total += last_spin

    await modify_cash(user_id, value=total)

    if total != 0:
        win_money_text = "You've own: " + str(round(total*100, 2)) + " zł!"
    else:
        win_money_text = ""

    await send_embed_msg(message, user_avatar_url, user_id, user_name, custom_text=win_money_text)


async def send_embed_msg(message, user_avatar_url, user_id, user_name, custom_text=""):
    new_message = jelonki.create_cash_embed(
        user_name=user_name, user_avatar_url=user_avatar_url, user_id=user_id
    )
    new_message.set_author(name=user_name)
    new_message.set_footer(text=custom_text)
    final_embed_msg = await message.channel.send(embed=new_message)
    await final_embed_msg.add_reaction('♻')
    await final_embed_msg.add_reaction('🥉')
    await final_embed_msg.add_reaction('🥈')
    await final_embed_msg.add_reaction('🥇')
    await final_embed_msg.add_reaction('🔊')
    await final_embed_msg.add_reaction('🔇')
