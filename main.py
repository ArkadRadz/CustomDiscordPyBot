import discord
import jelonki
import linie
import asyncio
import re
import messages
import setup
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
    command_emojis = ['♻️', '🥉', '🥈', '🥇', '🔊', '🔇']
    is_configured = False
    configure_message_id = 0
    self_vp = None

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            return

        try:
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)

            if self.is_configured is False and self.configure_message_id != 0 and payload.user_id == message.guild.owner_id:
                setup_msg = await message.channel.fetch_message(self.configure_message_id)
                if str(payload.emoji) not in self.command_emojis and not setup.is_setup_finished():
                    setup.set_emoji_symbol(setup.return_first_none_emoji(), str(payload.emoji))
                    emoji_to_set = setup.return_first_none_emoji()
                    if emoji_to_set is not None:
                        text_content = "React to this message with any emoji aside from " + " ".join(
                            self.command_emojis)
                        text_content = text_content + "to set as visible value: `" + emoji_to_set + "`"
                        await setup_msg.edit(content=text_content)
                        await setup_msg.clear_reactions()

                    setup.create_configuration(message.guild.id)
                    self.is_configured = setup.is_setup_finished()
            if self.is_configured is not False:
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
                    if payload.member.voice is not None:
                        if payload.member.voice.channel is not None:
                            channel = payload.member.voice.channel
                            self.self_vp = await channel.connect()
                            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("muzyka.mp3"), volume=0.15)
                            self.self_vp.play(source)
                            await messages.add_reactions(message)
                    else:
                        await channel.send(
                            "<!@{}> https://www.wykop.pl/cdn/c3201142/comment_ySeT49KshJdcuuoj9zkwOPvVLaulUvek.jpg".format(
                                payload.member.id))
                if payload.emoji.name == '🔇':
                    if payload.member.voice is not None:
                        if payload.member.voice.channel is not None or self.self_vp is not None:
                            await self.self_vp.disconnect()
                            await messages.add_reactions(message)
                    else:
                        await channel.send(
                            "<!@{}> https://www.wykop.pl/cdn/c3201142/comment_ySeT49KshJdcuuoj9zkwOPvVLaulUvek.jpg".format(
                                payload.member.id))


        except discord.HTTPException:
            pass

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$start'):
            await messages.print_bot_message(self, message)

        if message.content.startswith('$juz'):
            await message.channel.send("Czy mam ustawione emotki? " + str(setup.is_setup_finished()))
            await message.channel.send("Czy jestem skonfigurowany? " + str(self.is_configured))
            await message.channel.send(" ".join(setup.return_emoji_symbols().values()))

        if message.content.startswith('$sprzataj'):
            await self.clear_msg(message)

        if message.content.startswith('$avatar'):
            with open('avatar.jpg', 'rb') as f:
                image = f.read()

            await self.user.edit(avatar=image)

        if message.content.startswith('$zbigniew'):
            for attachment in message.attachments:
                await message.channel.send(attachment.url)

        if message.content.startswith('$czy'):
            user_id = '<@{}>'.format(str(message.author.id))
            if message.author.voice is not None:
                channel = message.author.voice.channel
                self.self_vp = await channel.connect()
                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("test.mp3"), volume=0.15)
                self.self_vp.play(source)
                await asyncio.sleep(10)
                await self.self_vp.disconnect()
            else:
                await message.channel.send(user_id + " https://www.youtube.com/watch?v=2vbYlqgWZk8")

        if message.content.startswith('$doladuj'):
            await jelonki.add_cash(message)

        if message.content.startswith('$daily'):
            await jelonki.add_daily_cash(message)

        if message.content.startswith('$hajs'):
            await jelonki.print_user_cash(client=self, message=message)

        if message.content.startswith('$set'):
            config = setup.read_configuration(message.guild.id)
            if config is not None:
                setup.emoji_symbols = config
                self.is_configured = setup.is_setup_finished()
                text_content = "Read existing configuration, set emoji to: " + " ".join(setup.emoji_symbols.values())
                await message.channel.send(text_content)

            if message.author.id == message.guild.owner_id and self.configure_message_id == 0 and self.is_configured is False:
                emoji_to_set = setup.return_first_none_emoji()
                text_content = "React to this message with any emoji aside from " + " ".join(self.command_emojis)
                text_content = text_content + "to set as visible value: `" + emoji_to_set + "`"
                setup_msg = await message.channel.send(text_content)
                self.configure_message_id = setup_msg.id

        if message.content.startswith('$nickname'):
            if message.author.id == message.guild.owner_id:
                await self.user.edit(username=message.content[10:])  # 10 due to length of $nickname with space

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
