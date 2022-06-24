import json
from re import L
from disnake import ApplicationCommandInteraction, Colour, Embed, Intents, TextChannel
import disnake
from disnake.ext import commands
from tools.EmbedHandler import EmbedHandler, YesNoEmbed
import os, config
from tools.json_work import *
from tools.insert import insert
import wikipedia

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config.prefix), intents=Intents.all(), help_command=None)

@bot.command()
async def help(inter:commands.Context, command = ''):
    await inter.message.add_reaction('➕')

@commands.has_role(config.owner_role_id)
@bot.command()
async def reload(inter: commands.Context, *, cog_name: str = None):
    if cog_name:
        bot.unload_extension(f'cogs.{cog_name}')
        bot.load_extension(f'cogs.{cog_name}')
    else:
        cogs = os.listdir('./cogs')
        for i in cogs:
            if i.endswith('.py'):
                name = i[:-3]
                bot.unload_extension(f'cogs.{name}')
                bot.load_extension(f'cogs.{name}')
    await inter.message.add_reaction('👍')

@commands.has_role(config.owner_role_id)
@bot.command()
async def rl(inter: ApplicationCommandInteraction, *, cog_name: str = None):
    await inter.message.add_reaction('👍')
    await reload(inter, cog_name=cog_name)

@bot.command()
async def echo(inter: ApplicationCommandInteraction, text: str = '', embed: bool = False):
    await inter.message.add_reaction('👍')
    if embed:
        embed = EmbedHandler(title=text)
        await inter.send(
            embed=embed.GetEmbed()
        )
    else:
        await inter.send(text)

@commands.has_role(config.owner_role_id)
@bot.command()
async def unload(inter: commands.Context, *, cog_name: str = None):
    await inter.message.add_reaction('👍')
    unloaded_cogs = []
    if cog_name:
        try:
            bot.unload_extension(f'cogs.{cog_name}')
        except:
            pass
        unloaded_cogs.append(cog_name)
    else:
        cogs = os.listdir('./cogs')
        for i in cogs:
            if i.endswith('.py'):
                name = i[:-3]
                bot.unload_extension(f'cogs.{name}')
                unloaded_cogs.append(name)
    embed = EmbedHandler(title='Выгруженные коги:')
    for i in range(len(unloaded_cogs)):
        embed.AddField(title=f'{i+1} ког:', description=unloaded_cogs[i], inline=False)
    await inter.send(
        embed=embed.GetEmbed()
    )

@commands.has_role(config.owner_role_id)
@bot.command()
async def load(inter: commands.Context, *, cog_name: str = None):
    await inter.message.add_reaction('👍')
    loaded_cogs = []
    if cog_name:
        try:
            bot.load_extension(f'cogs.{cog_name}')
        except:
            pass
        loaded_cogs.append(cog_name)
    else:
        cogs = os.listdir('./cogs')
        for i in cogs:
            if i.endswith('.py'):
                name = i[:-3]
                bot.load_extension(f'cogs.{name}')
                loaded_cogs.append(name)
    embed = EmbedHandler(title='Загруженные коги:')
    for i in range(len(loaded_cogs)):
        embed.AddField(title=f'{i+1} ког:', description=loaded_cogs[i], inline=False)
    await inter.send(
        embed=embed.GetEmbed()
    )

@bot.event
async def on_ready():
    print('бот готов')
    cogs = os.listdir('./cogs')
    for i in cogs:
        if i.endswith('.py'):
            name = i[:-3]
            bot.load_extension(f'cogs.{name}')
bot.run(config.token)