import discord
import jelonki
import linie
from datetime import datetime


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class MyClient(discord.Client):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.bg_task = self.loop.create_task(self.godzina_task())

    last_hajs_message_id = 0
    clearable_channel_id = 0

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            return

        try:
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)

            if payload.emoji.name == '♻':
                await jelonki.update_user_cash_message(message=message)

        except discord.HTTPException:
            pass

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$wojteg'):
            await message.channel.purge(limit=100)
            self.last_hajs_message_id = 0
            self.clearable_channel_id = 0

        if message.content.startswith('$sprzataj'):
            def is_me(m):
                if m.id == self.last_hajs_message_id:
                    self.last_hajs_message_id = 0
                return m.author == client.user

            await message.channel.purge(limit=100, check=is_me)

        if message.content.startswith('$doladuj'):
            await jelonki.add_cash(message)

        if message.content.startswith('$hajs'):
            await jelonki.print_user_cash(client=self, message=message)

        if message.content.startswith('$test'):
            game_board = jelonki.generate_field()

            game_board = jelonki.randomize_field(game_board)
            jelonki.print_field(game_board)
            embed_msg = discord.embeds.Embed(title="nie wiem jakaś gra",
                                             description=jelonki.print_discord_field(game_board))

            await message.channel.send(embed=embed_msg)
            rezultat = linie.check(1, game_board, w)
            print('ELUWINA')
            while rezultat[2]:
                print(rezultat[2])
                game_board = jelonki.regenerate_fields(game_board, w)
                linie.check(1, game_board, w)
                embed_msg = discord.embeds.Embed(title="nie wiem jakaś gra",
                                                 description=jelonki.print_discord_field(game_board))

                await message.channel.send(embed=embed_msg)
            await message.add_reaction("♻")

    # async def godzina_task(self):
    #     await self.wait_until_ready()
    #     while not self.is_closed():
    #         now = datetime.now()
    #         current_time = now.strftime("%H:%M")
    #         print (current_time)
    #         if current_time == "21:37":
    #             channel = self.get_channel()
    #             await channel.send("GODZINA")
    #             await channel.send("https://tenor.com/view/rat-jam-gif-19408520")
    #         else:
    #             await asyncio.sleep(30)


client = MyClient()

token = ''
try:
    token = open("token.txt", "r").read()
except IOError:
    print("File not accessible. Please create a token.txt with your discord token in it.")

client.run(token)
