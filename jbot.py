#J-Soc Bot
#Imports
import os
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'j!')
client.remove_command('help')
tvLinks = ['https://www.youtube.com/watch?v=7cw7rDLcujI', 
            'https://www.youtube.com/watch?v=MY2MPq0fbcM', 
            'https://www.youtube.com/watch?v=4gZpvVa0lis',
            'https://www.youtube.com/watch?v=VL3DF697-pQ',
            'https://www.youtube.com/watch?v=4lSO6t-VbdU',
            'https://www.youtube.com/watch?v=NRwSdXxg-10&list=PL526E93972CC5C3C0&index=2',
            'https://www.youtube.com/watch?v=BVD9AafJ3Vc&list=PL526E93972CC5C3C0&index=4',
            'https://www.youtube.com/watch?v=b7mbdXN7VPU',
            'https://www.youtube.com/watch?v=O8WKPpFARCs']


@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('Shogi'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('No command found.')

#Help command
@client.command()
async def help(ctx):

    embed = discord.Embed(
        colour = discord.Colour.red(),
        title = "J-Bot Help"
    )

    embed.add_field(name = 'Commands', value = 'help\nshogi\nevents\nwatch', inline = False)
    embed.set_thumbnail(url='https://japanesesoc.ucc.ie/wp-content/uploads/sites/98/2016/05/11233076_1144406582255394_7647945771561351557_n.png')
    await ctx.send(embed=embed)

@client.command()
async def events(ctx):
    await ctx.send('There are no upcoming events.')

@client.command()
async def shogi(ctx):
    await ctx.send('https://lishogi.org/')

@client.command()
async def watch(ctx):
    currentLink = random.choice(tvLinks)
    await ctx.send(currentLink)

client.run('XXXXXXXXXXXXXXXXX')
