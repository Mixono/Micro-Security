import discord
from colorama import *
import time
from discord.ext import commands
from discord.ui import Select, View
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='!ms ', intents=intents)

botwarnings = 'Off'
highlevelverification = 'Off'
mediumlevelverification = 'Off'
lowlevelverification = 'Off'
chatcooldown = 'Off'
chatmoderation = 'Off'
raidprotection = 'Off'
automoderation = 'Off'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Security Protocols'))
    print(Fore.CYAN + f'[ᴍɪᴄʀᴏ ꜱᴇᴄᴜʀɪᴛʏ]' + Fore.BLUE + f' Successfully logged in!' + Fore.WHITE + ' (' + Fore.GREEN + 'Passed' + Fore.WHITE + ')')
   
@client.command()
@commands.has_permissions(administrator = True)
async def lowlevelinfo(ctx):
    lowlevelembed = discord.Embed(title='Low Level Security', color=0x82FF33)
    lowlevelembed.add_field(name='Includes: ', value='Chat Cooldown, Chat Moderation & Low Level Verification', inline=True)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=lowlevelembed)
    

@client.command()
@commands.has_permissions(administrator = True)
async def mediumlevelinfo(ctx):
    mediumlevelembed = discord.Embed(title='Medium Level Security', color=0xFF5733)
    mediumlevelembed.add_field(name='Includes: ', value='Raid Protection, Auto Moderation, Bot Warnings & Medium level Verification ', inline=True)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=mediumlevelembed)
    

@client.command()
@commands.has_permissions(administrator = True)
async def highlevelinfo(ctx):
    highlevelembed = discord.Embed(title='High Level Security', color=0xFF3333)
    highlevelembed.add_field(name='Includes: ', value='Chat Cooldown, Chat Moderation, Raid Protection, Auto Moderation, High level Verification & Security Alerts ', inline=True)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=highlevelembed)

@client.command()
@commands.has_permissions(administrator = True)
async def lowlevel(interaction):
    lowleveloptions = Select(
        placeholder='Low Level Security Options',
        options=[
        discord.SelectOption(label='Chat Cooldown', emoji='🔒', description='Enable Chat Cooldown'),
        discord.SelectOption(label='Chat Moderation', emoji='🤐', description='Enable Chat Moderation'),
        discord.SelectOption(label='Low Level Verification (!ms verify)', emoji='✅', description='Enable Low Level Verification')
    ])
    async def my_callback(interaction):
        if lowleveloptions.values[0] == 'Chat Cooldown':
            chatcooldowncmd = discord.Embed(title=':beginner: *Enabled Chat Cooldown!*', color=0x82FF33)
            global chatcooldown
            chatcooldown = 'On'
            await interaction.response.send_message(embed=chatcooldowncmd)
       
        
        if lowleveloptions.values[0] == 'Chat Moderation':
            chatmoderationcmd = discord.Embed(title=':beginner: *Enabled Chat Moderation!*', color=0x82FF33)
            global chatmoderation
            chatmoderation = 'On'
            await interaction.response.send_message(embed=chatmoderationcmd)

        if lowleveloptions.values[0] == 'Low Level Verification (!ms verify)':
            lowverify = discord.Embed(title=':beginner: *Enabled Low Level Verification!*', color=0x82FF33)
            global lowlevelverification
            lowlevelverification = 'On'
            global mediumlevelverification
            mediumlevelverification = 'Off'
            global highlevelverification
            highlevelverification = 'Off'
            await interaction.response.send_message(embed=lowverify)

    lowleveloptions.callback = my_callback
    view = View()
    view.add_item(lowleveloptions)
    lowlevelcmd = discord.Embed(title=':beginner: Low Level Security Options', color=0x82FF33)
    await interaction.channel.purge(limit=1)
    await interaction.send(view=view, embed=lowlevelcmd)

@client.command()
@commands.has_permissions(administrator = True)
async def mediumlevel(interaction):
    mediumleveloptions = Select(
        placeholder='Medium Level Security Options',
        options=[
        discord.SelectOption(label='Bot Warnings', emoji='⚠️', description='Enable Bot Warnings'),
        discord.SelectOption(label='Raid Protection', emoji='⛔', description='Enable Raid Protection'),
        discord.SelectOption(label='Auto Moderation', emoji='🏆', description='Enable Auto Moderation'),
        discord.SelectOption(label='Medium Level Verification (!ms verify)', emoji='☢️', description='Enable Medium Level Verification')
    ])
    async def my_callback(interaction):
        if mediumleveloptions.values[0] == 'Bot Warnings':
            botwarningscmd = discord.Embed(title=':ringed_planet: *Enabled Bot Warnings!*', color=0xFF5733)
            global botwarnings
            botwarnings = 'On'
            await interaction.response.send_message(embed=botwarningscmd)

        if mediumleveloptions.values[0] == 'Raid Protection':
            raidprotectioncmd = discord.Embed(title=':ringed_planet: *Enabled Raid Protection!*', color=0xFF5733)
            global raidprotection
            raidprotection = 'On'
            await interaction.response.send_message(embed=raidprotectioncmd)

        if mediumleveloptions.values[0] == 'Auto Moderation':
            automoderationcmd = discord.Embed(title=':ringed_planet: *Enabled Auto Moderation!*', color=0xFF5733)
            global automoderation
            automoderation = 'On'
            await interaction.response.send_message(embed=automoderationcmd)


        if mediumleveloptions.values[0] == 'Medium Level Verification (!ms verify)':
            mediumverify = discord.Embed(title=':ringed_planet: *Enabled Medium Level Verification!*', color=0xFF5733)
            global mediumlevelverification
            mediumlevelverification = 'On'
            global lowlevelverification
            lowlevelverification = 'Off'
            global highlevelverification
            highlevelverification = 'Off'
            await interaction.response.send_message(embed=mediumverify)

    mediumleveloptions.callback = my_callback
    view = View()
    view.add_item(mediumleveloptions)
    mediumlevelcmd = discord.Embed(title=':ringed_planet: Medium Level Security Options', color=0xFF5733)
    await interaction.channel.purge(limit=1)
    await interaction.send(view=view, embed=mediumlevelcmd)

@client.command()
@commands.has_permissions(administrator = True)
async def highlevel(ctx):
    highlevelcmd = discord.Embed(title=':white_check_mark: Enabled High Level Security!', color=0xFF3333)
    highlevelcmd.add_field(name='Enabled: ', value='Chat Cooldown, Chat Moderation, Bot Moderation, High level Verification, Raid Protection & Alerts ', inline=True)
    global highlevel
    highlevel = 'On'
    global mediumlevel
    mediumlevel = 'Off'
    global lowlevel
    lowlevel = 'Off'
    global chatcooldown
    chatcooldown = 'On'
    global chatmoderation
    chatmoderation = 'On'
    global highlevelverification
    highlevelverification = 'On'
    global alerts
    alerts = 'On'
    global mediumlevelverification
    mediumlevelverification = 'Off'
    global lowlevelverification
    lowlevelverification = 'Off'
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=highlevelcmd)

@client.command()
@commands.has_permissions(administrator = True)
async def disable(ctx):
    disable = discord.Embed(title='Disabled Security', description=':no_entry_sign: Successfully disabled all security!', color=0xFF3333)
    global lowlevel
    lowlevel = 'Off'
    global mediumlevel
    mediumlevel = 'Off'
    global highlevel
    highlevel = 'Off'
    global highlevelverification
    highlevelverification = 'Off'
    global mediumlevelverification
    mediumlevelverification = 'Off'
    global lowlevelverification
    lowlevelverification = 'Off'
    global chatcooldown
    chatcooldown = 'Off'
    global chatmoderation
    chatmoderation = 'Off'
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=disable)

@client.command()
@commands.has_permissions(administrator = True)
async def info(ctx):
    helpcmd = discord.Embed(title=':question: Help Commands', color=0x82FF33)
    helpcmd.add_field(name='Prefix', value='!ms', inline=False)
    helpcmd.add_field(name='Low Level Security Command', value='!ms lowlevel', inline=False)
    helpcmd.add_field(name='Medium Level Security Command', value='!ms mediumlevel', inline=False)
    helpcmd.add_field(name='High Level Security Command', value='!ms highlevel', inline=False)
    helpcmd.add_field(name='Low Level Security Command Info', value='!ms lowlevelinfo', inline=False)
    helpcmd.add_field(name='Medium Level Security Command Info', value='!ms mediumlevelinfo', inline=False)
    helpcmd.add_field(name='High Level Security Command Info', value='!ms highlevelinfo', inline=False)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=helpcmd)

@client.command()
async def invite(ctx):
    invitecmd = discord.Embed(title=':wave: Bot Invite', color=0x82FF33)
    invitecmd.add_field(name='Current Bot Invite Link:', value='https://bit.ly/3hxGhsZ', inline=False)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=invitecmd)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    bancmd = discord.Embed(title=f':name_badge: Ban Information', color=0xFF3333)
    bancmd.add_field(name=f'Name:', value=f'{member.display_name}', inline=False),
    bancmd.add_field(name='ID:', value=f'{member.id}', inline=False),
    bancmd.add_field(name='Date Joined: ', value=f'{member.joined_at}', inline=False),
    bancmd.add_field(name='Reason Banned:', value=f'{reason}', inline=False)
    bannedmsg = discord.Embed(title=f':name_badge: You have been Banned!', color=0xFF3333)
    bannedmsg.add_field(name=f'Reason:', value=f'{reason}', inline=False),
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=bancmd)
    await member.ban(reason=reason)
    await member.send(embed=bannedmsg)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    kickcmd = discord.Embed(title=f':zap: Kick Information', color=0xFF3333)
    kickcmd.add_field(name=f'Name:', value=f'{member.display_name}', inline=False),
    kickcmd.add_field(name='ID:', value=f'{member.id}', inline=False),
    kickcmd.add_field(name='Date Joined: ', value=f'{member.joined_at}', inline=False),
    kickcmd.add_field(name='Reason Kicked:', value=f'{reason}', inline=False)
    kickedmsg = discord.Embed(title=f':zap: You have been Kicked!', color=0xFF3333)
    kickedmsg.add_field(name=f'Reason:', value=f'{reason}', inline=False),
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=kickcmd)
    await member.kick(reason=reason)
    await member.send(embed=kickedmsg)

client.run('MTA0MDQ1MTQxMDUyMjgwNDM0NQ.GUxtXw.V5HEHaWaYpeot_NpUBSPfhEwjoXIfKk4o_Jrb4')
