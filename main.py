import discord
import jelonki
import linie
import asyncio
import re
from datetime import datetime
from discord.ext import commands

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
    last_game_board_message_id = 0
    clearable_channel_id = 0
    self_vp = None

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
                await jelonki.update_user_cash_message(payload=payload, message=message)
            if payload.emoji.name == '🥉':
                await self.clear_msg(message)
                await linie.spin(message=message, bet="50", payload=payload)
            if payload.emoji.name == '🥈':
                await self.clear_msg(message)
                await linie.spin(message=message, bet="100", payload=payload)
            if payload.emoji.name == '🥇':
                await self.clear_msg(message)
                await linie.spin(message=message, bet="500", payload=payload)
            if payload.emoji.name == '🔊':
                if payload.member.voice.channel is not None:
                    channel = payload.member.voice.channel
                    self.self_vp = await channel.connect()
                    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("muzyka.mp3"), volume=0.15)
                    self.self_vp.play(source)
                    await message.clear_reactions()
                    await message.add_reaction('♻')
                    await message.add_reaction('🥉')
                    await message.add_reaction('🥈')
                    await message.add_reaction('🥇')
                    await message.add_reaction('🔊')
                    await message.add_reaction('🔇')
            if payload.emoji.name == '🔇':
                if payload.member.voice.channel is not None or self.self_vp is not None:
                    await self.self_vp.disconnect()
                    await message.clear_reactions()
                    await message.add_reaction('♻')
                    await message.add_reaction('🥉')
                    await message.add_reaction('🥈')
                    await message.add_reaction('🥇')
                    await message.add_reaction('🔊')
                    await message.add_reaction('🔇')

        except discord.HTTPException:
            pass

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$wojteg'):
            await message.channel.purge(limit=100)
            self.last_hajs_message_id = 0
            self.clearable_channel_id = 0

        if message.content.startswith('$start'):
            react1 = "React with ♻ to check your account balance"
            react2 = "React with 🥉 to spin for 0.50 zł"
            react3 = "React with 🥈 to spin for 1zł"
            react4 = "React with 🥇 to spin for 5zł"
            react5 = "Turn music on with 🔊 or off with 🔇"
            react_msg = react1 + "\n" + react2 + "\n" + react3 + "\n" + react4 + "\n" + react5

            embed_msg = discord.embeds.Embed(
                title="JELONKI",
                description=react_msg,
            )
            embed_msg.set_author(name=message.author.name)
            embed_msg.set_thumbnail(
                url="https://cdnroute.bpsgameserver.com/contenthub-cdn-origin/media/casinoeuro/casinoeuro_blog/27167_Monthly_Hightlights_Northern_sky.jpg")

            embed = await message.channel.send(embed=embed_msg)
            await embed.add_reaction('♻')
            await embed.add_reaction('🥉')
            await embed.add_reaction('🥈')
            await embed.add_reaction('🥇')
            await embed.add_reaction('🔊')
            await embed.add_reaction('🔇')

        if message.content.startswith('$sprzataj'):
            await self.clear_msg(message)

        if message.content.startswith('$doladuj'):
            await jelonki.add_cash(message)

        if message.content.startswith('$hajs'):
            await jelonki.print_user_cash(client=self, message=message)

        if message.content.startswith('$test'):
            await self.clear_msg(message)
            await linie.spin(message)

    async def clear_msg(self, message):
        def is_me(m):
            if m.id == self.last_hajs_message_id:
                self.last_hajs_message_id = 0
            return m.author == client.user

        await message.channel.purge(limit=100, check=is_me)

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
