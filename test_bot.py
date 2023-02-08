import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(1065058202867220550))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTA2NTA1ODIwMjg2NzIyMDU1MA.GteAQF.L1LtCd0R-Eu3Hs5yykpuGtYMBqL45flELLgPsc')
