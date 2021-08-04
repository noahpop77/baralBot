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


@BaralBot.command(pass_context=True)
async def ssh(ctx, *, message):
    with paramiko.client.SSHClient() as client:
        #adds auto policy if none are present and deals with "not found in known_hosts" errors
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #socket.getaddrinfo('192.168.2.154', 22)

        #connects to the actual machine with the specified information
        client.connect(' 		', username='berna', password='pass', look_for_keys=False, allow_agent=False)
        print("Command Established!...")
        #input output error
        stdin, stdout, stderr = client.exec_command(message)

        #sets output of the commands equal to lines in list format
        lines = stdout.readlines()
        print("Command Executed!...")
        output = ""
        if client.recv_exit_status() == 0:
            #prints it nice and pretty
            for line in lines:
                output = output + line
        
        print(output)
        print("Connection closed!...")
        await BaralBot.send_message(BaralBot.get_channel("534097326659076106"), "Command Executed!...")
        await BaralBot.say(output)


#just a simple help menu
@BaralBot.command()
async def halp():
	halp = """
	```
	---------------------------------------------------------------------
	Help Menu

	`word	-	Takes in a string as input and produces stylish text
	`ssh 	-	Takes input in the form of a string and uses that string as a command

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
