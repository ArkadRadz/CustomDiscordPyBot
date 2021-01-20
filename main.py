import discord
import jelonki
import linie

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            return

        try:
            if str(payload.emoji) == "♻️":
                channel = client.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                await message.clear_reactions()
                # TODO: set emoji to execute reroll
        except discord.HTTPException:
            pass

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

        if message.content.startswith('$test'):
            gameboard = jelonki.generate_field()

            gameboard = jelonki.randomize_field(gameboard)
            jelonki.print_field(gameboard)
            embedMsg = discord.embeds.Embed(title="nie wiem jakaś gra", description=jelonki.print_discord_field(gameboard))

            await message.channel.send(embed=embedMsg)
            rezultat = linie.check(1, gameboard, w)
            print('ELUWINA')
            while rezultat[2]:
                print(rezultat[2])
                gameboard = jelonki.regenerate_fields(gameboard, w)
                linie.check(1, gameboard, w)
                embedMsg = discord.embeds.Embed(title="nie wiem jakaś gra",
                                                description=jelonki.print_discord_field(gameboard))

                await message.channel.send(embed=embedMsg)
            await message.add_reaction("♻")

client = MyClient()

token = open("token.txt", "r").read()

client.run(token)
