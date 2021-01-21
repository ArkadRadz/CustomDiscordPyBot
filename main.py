import discord
import jelonki
import linie
import users


def get_printable_user_cash(user_id):
    user_cash = int(users.read_user_data(user_id)) / 100

    return str(user_cash)


class MyClient(discord.Client):
    last_hajs_message_id = 0

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            return

        try:
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)

            if payload.emoji.name == '♻':
                await message.clear_reactions()

                embed_msg = discord.embeds.Embed(
                    title="Twoje hajsy to: " + get_printable_user_cash(payload.user_id) + " zł",
                    description="TODO"
                )

                embed_msg.set_author(name=payload.member.name)
                embed_msg.set_thumbnail(url=payload.member.avatar_url)

                await message.edit(embed=embed_msg)
                await message.add_reaction('♻')

                # TODO: set emoji to execute reroll

        except discord.HTTPException:
            pass

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

        if message.content.startswith('$wojteg'):
            await message.channel.purge(limit=100)

        if message.content.startswith('$sprzataj'):
            def is_me(m):
                return m.author == client.user

            await message.channel.purge(limit=100, check=is_me)

        if message.content.startswith('$hajs'):
            if self.last_hajs_message_id != 0:
                last_hajs_message = await message.channel.fetch_message(self.last_hajs_message_id)
                await message.channel.delete_messages([last_hajs_message])

            embed_msg = discord.embeds.Embed(
                title="Twoje hajsy to: " + get_printable_user_cash(message.author.id) + " zł",
                description="TODO"
            )

            embed_msg.set_author(name=message.author.name)
            embed_msg.set_thumbnail(url=message.author.avatar_url)

            new_message = await message.channel.send(embed=embed_msg)
            self.last_hajs_message_id = new_message.id
            await new_message.add_reaction('♻')

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


client = MyClient()

token = ''
try:
    token = open("token.txt", "r").read()
except IOError:
    print("File not accessible. Please create a token.txt with your discord token in it.")

client.run(token)
