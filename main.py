# Things to add #
# Create code for the Embed Creator command
# Make a error message for both the console and in the discord

import discord
import os
import configparser
from discord.ext import commands
from discord import Embed, Emoji
from asyncio import sleep

# Read Config.ini File
config = configparser.ConfigParser()
config.read(os.path.abspath(__file__).replace(os.path.basename(__file__), "config.ini"))

# Tokens
DiscordToken = config["Discord"]["discordToken"]

intents = discord.Intents.default()
intents.members = True
intents.messages = True

# Bots Prefix
client = commands.Bot(intents=intents, command_prefix = "$")

# Removes the basic discord Help command
client.remove_command("help")

# Will show that the Bot is online in console
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print(f'{client.user} has logged in')

# Member count when someone joins
@client.event
async def on_member_join(member):
    true_member_count = len([m for m in member.guild.members if not m.bot])
    for channel in member.guild.channels: 
	    if channel.name.startswith('Members'):
		    await channel.edit(name=f'Members: {true_member_count}')

# Member count when someone leaves
@client.event
async def on_member_remove(member):
    true_member_count = len([m for m in member.guild.members if not m.bot])
    for channel in member.guild.channels: 
	    if channel.name.startswith('Members'):
		    await channel.edit(name=f'Members: {true_member_count}')

# Help command
@client.command()
@commands.has_permissions(kick_members = True)
async def help(ctx, specific = None):
    await ctx.message.delete()
    if specific == "create":
        helpcreate = discord.Embed(title= "How To Create a Embed", description= "This is still a Work In Progress", color= discord.Colour.red())
        await ctx.send(embed=helpcreate)
    elif specific == None:
        helpem = discord.Embed(title= "The Bot Prefix Is $", description= "", color= discord.Colour.red())
        helpem.add_field(name="`$help create`", value="This will show you how to create your own Embed.", inline= False)
        helpem.add_field(name="`$[Channel]`", value="""This will post the pre-existing Embeds created for specific channels.
        
        **Channels**
        modcommand""", inline= False)
        await ctx.send(embed=helpem)

# Embed creator WIP
@client.command()
@commands.has_permissions(kick_members = True)
async def create(ctx):
    await ctx.message.delete()
    await ctx.send()

# Emoji debug
@client.command(pass_context=True)
async def debug(ctx, emoji: Emoji):
    await ctx.message.delete()
    emembed = Embed(description=f"emoji: {emoji}", title=f"emoji: {emoji}")
    emembed.add_field(name="id", value=repr(emoji.id))
    emembed.add_field(name="name", value=repr(emoji.name))
    await ctx.send(embed=emembed)

# Welcome embed
@client.command()
@commands.has_permissions(administrator = True)
async def welcome(ctx):
    await ctx.message.delete()
    welem = discord.Embed(title= "Welcome to The Ctrl Discord Server", description= "Welcome to the official Ctrl Rust community Discord server. Here you will find the latest information regarding our Rust servers, additionally you can find links to our website and Rust servers.", color= discord.Colour.red())
    welem.set_thumbnail(url="https://i.imgur.com/QVI0qY0.jpg")
    welem.add_field(name="Important Channels", value="""**Our Rules: <#922164189055827968>**
**Announcements: <#928436720016441434>**
**Discord Security Tips: <#928438324568412160>**
**Server Information: <#921987422621941830>**
**Staff Application: <#922190083598217227>**""",inline= False)
    welem.add_field(name="Main Links", value= """<:www:927806473893978132> Website: [Click Here](https://epokleague.com/ctrl/)
    <:cart:927806387608764427> Store: [Click Here](https://epokleague.com/shop-page/)
    """,inline= False)
    welem.add_field(name="Our Rust server <:rust:927806738487476285>", value="steam://connect/104.0.42.115:28015",inline= False)
    await ctx.send(embed=welem)

# Rules embed
@client.command()
@commands.has_permissions(administrator = True)
async def rules(ctx):
    await ctx.message.delete()
    rulem = discord.Embed(title= "Ctrl Discord Rules", description= """We ask that you abide by the following rules in order to maintain a positive and friendly experience for all members.
    
All content must be in accordance with the Discord [Terms of Service](https://discord.com/terms) and [Community Guidelines](https://discord.com/guidelines)

This is an English-speaking server. Please keep all conversations in text or voice channels in English.""", color= discord.Colour.red())
    rulem.add_field(name=":mute: Mutable Violations", value=""":yellow_circle: Chat Spam and/or Flooding
:yellow_circle: Racist or Discriminatory Conduct (i.e. Homophobia)
:yellow_circle: Unapproved Advertising (i.e. External Communities)
:yellow_circle: Disrespect/Harassment of Staff/Community Members
:yellow_circle: Rule-baiting
:yellow_circle: Attempting to Bypass Word Filter""", inline=False)
    rulem.add_field(name="<:ban:927824178755809291> Bannable Violations", value=""":red_circle: Cheating and/or Use of Malicious Software
:red_circle: Threats of Harm and/or Self-Inflicted Injury
:red_circle: Encouraging Self-Inflicted Injury
:red_circle: Disclosure of Personal/Private Information (i.e. DOXing)
:red_circle: Threats of Distributed Denial-of-Service Attacks (i.e. DDoSing)
:red_circle: Circumventing an existing punishment through the use of an alternate account""", inline=False)
    rulem.add_field(name=":shield: Enforcement", value="""<@&921992005444333608>, <@&921992230577778708>, <@&927858269572194305> & <@&921990482928734248> have the discretion to give out punishments for reasons not directly stated above. Those responsible for enforcing these rules have the final say.
    
    Our Moderation team are to be held accountable and are expected to follow the outlined rules. Any misconduct including not enforcing the rules, not following the rules or abuse of their power should be reported immediately to the <@&927858269572194305>.""",inline=False)
    await ctx.send(embed=rulem)

# Rust Server Info
@client.command()
@commands.has_permissions(administrator = True)
async def info(ctx):
    await ctx.message.delete()
    infoem = discord.Embed(title= "CTRL Vanilla Server by Epokleague.com", url= "https://epokleague.com/rust/", description="""**200 Population**
    **Thursday Weekly Wipe Schedule**
    **Monthly Blueprint Wipes**
    **Strong Admin and Moderator Support Staff**""", color= discord.Color.red())
    infoem.set_thumbnail(url="https://i.imgur.com/vFsdKjR.png")
    await ctx.send(embed=infoem)
    servem = discord.Embed(title= "<:rust:927806738487476285> North American Rust Server", color= discord.Color.red())
    servem.add_field(name="Vanilla (Medium): steam://connect/104.0.42.115:28015",value="`client.connect 104.0.42.115:28015`")
    await ctx.send(embed=servem)

# Security Tips
@client.command()
@commands.has_permissions(administrator = True)
async def tips(ctx):
    await ctx.message.delete()
    tipsem = discord.Embed(title= "Security Tips", description= "As our community grows, we will start to see an uptake of scammers and malicious user trying to cause harm to the members of our server. Here is a list of precautionary measures you should follow to keep your account safe.", color= discord.Colour.red())
    await ctx.send(embed=tipsem)
    tips1em = discord.Embed(title= "Tip #1 - Inspect Links Before Accesing Them.", description= "Links can be manipulated in lots of ways. We urge you to __**Never**__ click on a link you do not recognize! If you are unsure that the link is trustworthy run it thru a scanner like [VirusTotal](https://www.virustotal.com/gui/home/url).", color= discord.Colour.red())
    await ctx.send(embed=tips1em)
    tips2em = discord.Embed(title= "Tip #2 - Nothing Spontaneous Is Free.", description= "If you receive a message about winning a prize that you __didn't sign up for__... **It's a scam!** Discord servers will announce winners in their respective servers, not thru DM's. Genuine offers for free **Discord Nitro** will never be awarded thru direct messages. If you receive a message asking to visit a website to redeem rewards or prizes, **it is a scam!**", color= discord.Colour.red())
    await ctx.send(embed=tips2em)
    tips3em = discord.Embed(title= "Tip #3 - Use Two-Factor Authentication.", description= "We **strongly** recommend that everyone enables Two-Factor Authentication **(2FA)** on their accounts. This provides an extra layer of security against unauthorized sign-in attempts. If you would like more information about 2FA, visit [Discord Two-Factor Authentication](https://support.discord.com/hc/en-us/articles/219576828-Setting-up-Two-Factor-Authentication) or [Steam Guard](https://help.steampowered.com/en/faqs/view/6639-EB3C-EC79-FF60).", color= discord.Colour.red())
    await ctx.send(embed=tips3em)
    tips4em = discord.Embed(title= "Tip #4 - Disabling DM's From Server Members", description= "These actions will negate scam attemps on your account.", color= discord.Colour.red())
    tips4em.add_field(name="Disable DM's from Server Members (Server-Specific) - Effective" ,value="To disable direct messages from members of a specific server, right-clicking the server icon, click on `Privacy Settings` and uncheck the option `Allow direct messages from server members`.",inline=False)
    tips4em.add_field(name="Disable DM's from Server Members (Globally) - Recommended" ,value="To disable direct messages from members of all servers, click on the gear icon :gear: on the bottom left of your Discord screen, access `Privacy & Safety` and uncheck the option `Allow direct messages from server members`. This will only apply to new servers that you join from that point on, you will need to go through individual servers and disable this option using the method shown above.",inline=False)
    await ctx.send(embed=tips4em)

# Bot commands embed
@client.command()
@commands.has_permissions(administrator = True)
async def tatsuhelp(ctx):
    await ctx.message.delete()
    tatsuem = discord.Embed(title= "Bot Commands FAQ", description= """The following is a list of commands you can use via our . The prefix is t!

Not all commands will be listed, just the key ones. For a full list do t!help""", color= discord.Colour.red())
    tatsuem.add_field(name="Rewards and Economy Commands", value=""":point_right: t!dailies (Can also do t!daily)
Get free credits daily! Can be given to others for a boosted amount.

:point_right: t!points (Can also do t!point)
Check a user's server points or give your points to someone.

:point_right: t!wallet
Displays a user's currencies.

:point_right: t!inventory
Opens your inventory.

:point_right: t!shop (Can also do t!buy)
Opens the shop menu to access the event shop, expedition store, or global store.

:point_right: t!item (Can also do t!use / t!items or t!useitem)
A faster way of viewing/using items.

:point_right: t!exchange
Convert credits to/from tradeable credits (there is tax!). Tradeable credits can be traded to others using t!trade.

:point_right: t!quests
Shows your quests and claims completed quests.

:point_right: t!trade
Manage trades with other users.""",inline=False)
    tatsuem.add_field(name="Social Commands", value=""":point_right: t!rank
View a user's rank.

:point_right: t!profile
View a user's profile.

:point_right: t!reputation
Award someone a reputation point.

:point_right: t!top
Global/Server XP Rankings

:point_right: t!badges
Manages your badges

:point_right: t!background
Redirects users to the dashboard where they can change their profile background.

:point_right: t!house
View and edit your house!

:point_right: t!country
Sets your country. This can be viewed in your profile.

:point_right: t!settag
Set your profile tag. This can be viewed in your profile.""", inline=False)
    tatsuem.add_field(name="Game Commands",value=""":point_right: t!tatsugotchi
Take care of a cute Tatsugotchi and interact with it!

:point_right: t!daycare
The daycare allows you to customize as many pets & room layouts as you want.

:point_right: t!fish
Cast your line for a fish!

:point_right: t!slots
Play some slots!

:point_right: t!cookie
Give someone cookies.""", inline=False)
    await ctx.send(embed=tatsuem)

# Mod commands embed
@client.command()
@commands.has_permissions(administrator = True)
async def modcommand(ctx):
    await ctx.message.delete()
    commandem = discord.Embed(title= "Here is a list of the commands available", description= """
""", color= discord.Colour.red())
    await ctx.send(embed=commandem)

client.run(DiscordToken)