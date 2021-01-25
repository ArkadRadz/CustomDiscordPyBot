import discord


async def print_bot_message(self, message):
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
    await add_reactions(message)


async def add_reactions(message):
    await message.clear_reactions()
    await message.add_reaction('♻')
    await message.add_reaction('🥉')
    await message.add_reaction('🥈')
    await message.add_reaction('🥇')
    await message.add_reaction('🔊')
    await message.add_reaction('🔇')
