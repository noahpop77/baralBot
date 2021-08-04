#!/usr/bin/python3

import asyncio
import asyncore
import sys
import pyfiglet
from pyfiglet import figlet_format
import socket
import paramiko
import random
import os
import discord
from discord.ext import commands

BaralBot = commands.Bot(command_prefix='`')

@BaralBot.event
async def on_ready():
    os.system("clear")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Brian Sawa")
    print("January 2019")
    print("READY WHEN YOU ARE :^)")
    print("I am running on: " + BaralBot.user.name)
    print("Version: " + str(discord.version_info))
    print("With the ID: " + BaralBot.user.id)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#just a simple help menu
@BaralBot.command()
async def halp():
	halp = """
	```
	---------------------------------------------------------------------
	Help Menu

	`word	-	Takes in a string as input and produces stylish text

	---------------------------------------------------------------------
	```
	"""
	await BaralBot.say(halp)

#PRINTS SOMETHING TO THE CONSOLE WHEN SOMEONE SENDS A MESSAGE
@BaralBot.event
async def on_message(message):
    if message.author.bot==False:
        print("Messages sent")
        await BaralBot.process_commands(message)

#This command takes input and produces ascii word art in its place
@BaralBot.command(pass_context=True)
async def word(ctx, *, message):
    mainout = figlet_format(message, font='starwars')
    await BaralBot.delete_message(ctx.message)
    await BaralBot.say("```" + mainout + "```")


BaralBot.run("DiscordAPIKey")
