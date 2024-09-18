import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked.')
    else:
        await ctx.send('You do not have permission to kick members.')

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned.')
    else:
        await ctx.send('You do not have permission to ban members.')

@bot.command()
async def mute(ctx, member: discord.Member, duration: int, *, reason=None):
    if ctx.author.guild_permissions.manage_roles:
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if mute_role:
            await member.add_roles(mute_role)
            await ctx.send(f'{member} has been muted for {duration} minutes.')
            await asyncio.sleep(duration * 60)  # Mute duration in seconds
            await member.remove_roles(mute_role)
            await ctx.send(f'{member} has been unmuted.')
        else:
            await ctx.send('Mute role not found.')
    else:
        await ctx.send('You do not have permission to mute members.')

@bot.command()
async def lock(ctx, channel: discord.TextChannel):
    if ctx.author.guild_permissions.manage_channels:
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(f'{channel} has been locked.')
    else:
        await ctx.send('You do not have permission to lock channels.')

bot.run('YOUR_BOT_TOKEN')
