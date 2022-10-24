import discord, os, sys, colorama, json
from discord.ext import commands
from colorama import Fore, Style, Back


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

intents = discord.Intents.all()
intents.members = True
intents.guilds = True

client = commands.Bot(command_prefix=prefix,
                      case_insensitive=True,
                      intents=intents)
client.remove_command('helps')


@client.event
async def on_ready():
    print(f'{client.user} is online!')


@client.command()
async def dmall(ctx, *, args=None):
    ownerID = BOT OWNER ID
    if ctx.message.author.id == ownerID:
        if args != None:
            members = ctx.guild.members
            for member in members:
                try:
                    await member.send(args)
                    print("'" + args + "' was sent to" + member.name)
                except:
                    print("Couldn't send'" + args + "' to " + member.name)
        else:
            await ctx.send('Could provide an argument!')
    else:
        await ctx.send('You do not have the permissions for this command!')


client.run(token)
