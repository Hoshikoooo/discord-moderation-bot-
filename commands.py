import discord
from discord.ext import commands

async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

async def mute(ctx, member: discord.Member, duration: int, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if not role:
        role = await ctx.guild.create_role(name='Muted')
        for channel in ctx.guild.channels:
            await channel.set_permissions(role, speak=False, send_messages=False)
    await member.add_roles(role, reason=reason)
    await ctx.send(f'Muted {member.mention} for {duration} minutes')
    await asyncio.sleep(duration * 60)
    await member.remove_roles(role)
    await ctx.send(f'Unmuted {member.mention}')

async def lock(ctx):
    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send('Server has been locked.')

def setup(bot):
    bot.add_command(commands.Command(kick, name='kick'))
    bot.add_command(commands.Command(ban, name='ban'))
    bot.add_command(commands.Command(mute, name='mute'))
    bot.add_command(commands.Command(lock, name='lock'))