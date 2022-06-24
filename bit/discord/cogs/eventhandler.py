import asyncio
import inspect
import os
import disnake
from disnake.ext import commands
from disnake import ClientException, Embed, Interaction, InteractionType, Member, Message, Guild, Client, MessageInteraction, TextChannel
from disnake.ui import View, Button
import config, re
from tools.EmbedHandler import EmbedHandler
from tools.EmbedHandler import YesNoEmbed

class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(
                embed=YesNoEmbed(
                    'Были пропущены или добавлены лишние аргументы. \nПосмотрите `!help <command>` для лучшего ознакомления',
                    False
                ).GetEmbed()
            )
        if isinstance(error, commands.MissingPermissions):
            print(error)
            await ctx.send(embed=Embed(
                title='Ошибка',
                description='У вас не хватает прав',
                color=disnake.Color.red())
            )
        elif isinstance(error, commands.BotMissingPermissions):
            print(error)
            await ctx.send(embed=Embed(
                title='Ошибка',
                description='У бота не хватает прав',
                color=disnake.Color.red())
            )
        elif isinstance(error, commands.CommandInvokeError):
            print(error)
            await ctx.send(embed=Embed(
                title='Ошибка',
                description='Ошибка со стороны бота',
                color=disnake.Color.red())
            )
        elif isinstance(error, commands.CommandOnCooldown):
            print(error)
            await ctx.send(embed=Embed(
                title='Ошибка',
                description='Команда на кулдауне',
                color=disnake.Color.red())
            )
        elif isinstance(error, commands.BadArgument):
            print(error)
            await ctx.send(embed=Embed(
                title='Ошибка',
                description='Неправильные аргументы',
                color=disnake.Color.red())
            )
        elif isinstance(error, commands.ObjectNotFound):
            await ctx.send(embed=Embed(
                title='Ошибка',
                description='Не удалось загрузить',
                color=disnake.Color.red())
            )
        elif isinstance(error, asyncio.TimeoutError):
            await ctx.send(
                embed=YesNoEmbed(
                    'Не хватило времени на подключение',
                    False
                ).GetEmbed()
            )
        elif isinstance(error, ClientException):
            await ctx.send(
                embed=YesNoEmbed(
                    'Бот уже подключён',
                    False
                ).GetEmbed()
            )
        elif isinstance(error, disnake.opus.OpusNotLoaded):
            await ctx.send(
                embed=YesNoEmbed(
                    'Какой то opus не загрузился',
                    False
                ).GetEmbed()
            )
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send(
                embed=YesNoEmbed(
                    'Вы феминистка',
                    False
                ).GetEmbed()
            )

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        await member.guild.get_channel(config.newcoming_id).send(
            embed=EmbedHandler(title='Новый участник', description=member.mention).GetEmbed()
        )

    @commands.Cog.listener()
    async def on_member_remove(self, member: Member):
        print(member, member.guild)

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        def get_urls(text: str):
            if len(re.findall(config.url_regex, text, re.IGNORECASE)):
                return re.findall(config.url_regex, text, re.IGNORECASE)
            return None

        ban_words = re.findall(config.russian_ban_word, message.content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.VERBOSE)
        if len(ban_words) and not message.author.bot:
            await message.delete()
            await message.channel.send(
                embed = YesNoEmbed(
                    'Нельзя материться на этом сервере',
                    False
                ).GetEmbed()
            )

        if get_urls(message.content):
            for i in get_urls(message.content):
                for j in config.banned_hosts:
                    if i.startswith(j):
                            await message.delete() 
                            await message.author.send(
                                embed=YesNoEmbed(
                                    "Нельзя размещать запрещённые ссылки",
                                    False
                                ).GetEmbed()
                            )
                            return
                    else:
                        await message.author.send(
                            embed=YesNoEmbed(
                                "Плохо размещать небезопасные ссылки",
                                False
                            ).GetEmbed()
                        )
                        return

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload:disnake.raw_models.RawReactionActionEvent):
        guild: Guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        c = await channel.fetch_message(payload.message_id)
        content = c.content

        if not payload.member.bot and (content.startswith('!rl') or content.startswith('!reload')):
            cog_name = ''
            loaded_cogs = []
            command = content.split(' ')
            if len(command) > 1:
                cog_name = command[1]
            if cog_name:
                self.bot.unload_extension(f'cogs.{cog_name}')
                self.bot.load_extension(f'cogs.{cog_name}')
                loaded_cogs.append(cog_name)
            else:
                cogs = os.listdir('./cogs')
                for i in cogs:
                    if i.endswith('.py'):
                        name = i[:-3]
                        self.bot.unload_extension(f'cogs.{name}')
                        self.bot.load_extension(f'cogs.{name}')
                        loaded_cogs.append(name)
            embed = EmbedHandler(title='Загруженные коги:')
            for i in range(len(loaded_cogs)):
                embed.AddField(title=f'{i+1} ког:', description=loaded_cogs[i], inline=False)
            await channel.send(
                embed=embed.GetEmbed()
            )
        
        elif not payload.member.bot and (content.startswith('!help')):
            def createcommand(hlpcommand):
                command.append(Button(label=hlpcommand.name, custom_id=hlpcommand))
                params = list(hlpcommand.params.keys())[2:]
                com = ''
                for param in params:
                    if hlpcommand.params[param].default != inspect._empty:
                        com += f' `{hlpcommand.params[param].name}`(Optional)'
                    else:
                        com += f' `{hlpcommand.params[param].name}`(Required)'
                return com

            def cogcommands(hlpcommand):
                output = f'__**{hlpcommand}**__\n'
                if hlpcommand == 'Main':
                    cog = []
                    for i in self.bot.commands:
                        if not i.cog_name:
                            cog.append(i)
                else:
                    cog = self.bot.cogs[hlpcommand].get_commands()
                for comm in cog:
                    com = createcommand(comm)
                    output += f'`!{comm.name}`{com}\n'
                return output

            output = ''
            command = content.split()
            commands = dict()
            hlpcommand = ''
            if len(command) > 1:
                hlpcommand = command[1]
            topics = list(self.bot.cogs.keys())
            topics.append('Main')
            if hlpcommand in topics:
                output += cogcommands(hlpcommand)
                await channel.send(
                    embed=EmbedHandler(
                        title='Cписок команд',
                        description=output
                    ).GetEmbed()
                )
            elif hlpcommand:
                hlpcommand = self.bot.get_command(hlpcommand)
                com = createcommand(hlpcommand)
                print(com)
                output += f'`!{hlpcommand.name}`{com}'
                await channel.send(
                    embed=EmbedHandler(
                        title='Cписок команд',
                        description=output
                    ).GetEmbed()
                )
            else:
                cats = dict()   
                for i in self.bot.commands:
                    hlpcommand = self.bot.get_command(i.name)
                    cog_name = hlpcommand.cog_name
                    if not cog_name:
                        cog_name = 'Main'
                    out = f'`!{hlpcommand.name}` '
                    try:
                        cats[cog_name] += out
                    except:
                        cats[cog_name] = out

                keys = []
                for i in cats.keys():
                    keys.append(i)
                keys.sort()
                for i in keys:
                    commands[i] = Button(label=i, custom_id=i)
                    output += f"\n__**{i}**__\n{cats[i]}"

                await channel.send(
                    embed=EmbedHandler(
                        title='Cписок команд',
                        description=output
                    ).GetEmbed()
                )
                view = View()
                for i in commands:
                    view.add_item(commands[i])

                await channel.send(view=view)

                def check(inter: MessageInteraction):
                    return inter

                ctx:MessageInteraction = await self.bot.wait_for('button_click', check=check)
                output = cogcommands(ctx.component.label)
                await ctx.response.send_message(embed=EmbedHandler(
                        title='Cписок команд',
                        description=output
                    ).GetEmbed()
                )
                
        if payload.channel_id == config.mood_channel_id:
            emoji = payload.emoji
            print(emoji, emoji.name)
            guild = self.bot.get_guild(payload.guild_id)
            await Guild.get_member(guild, payload.user_id).add_roles(guild.get_role(config.emojis[emoji.name])) 

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload:disnake.raw_models.RawReactionActionEvent):  
        guild = self.bot.get_guild(payload.guild_id)
        channel: TextChannel = guild.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        content = message.content

        if content.startswith('!rl') or content.startswith('!reload'):
            history = await channel.history().flatten()
            for i in range(len(history)):
                if history[i].id == message.id:
                    await history[i-1].delete()
                    break

        if content.startswith('!help'):
            history = await channel.history().flatten()
            for i in range(len(history)):
                if history[i].id == message.id:
                    await history[i-2].delete()
                    await history[i-1].delete()
                    break

        if payload.channel_id == config.mood_channel_id:
            emoji = payload.emoji
            print(emoji, emoji.name, payload.user_id)
            await Guild.get_member(guild, payload.user_id).remove_roles(guild.get_role(config.emojis[emoji.name])) 
  

def setup(bot):
    bot.add_cog(EventHandler(bot))