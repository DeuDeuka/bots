import asyncio
import random
from disnake import ApplicationCommandInteraction, Attachment, ButtonStyle, Colour, Embed, Emoji, InteractionResponded, InteractionType, Message, MessageInteraction, Option, OptionType, PermissionOverwrite, SelectOption
import disnake
from disnake.ext import commands
from requests import options
from tools.parser import Parser
from tools.getseconds import getseconds
from tools.EmbedHandler import EmbedHandler, YesNoEmbed
import config
import json
from disnake.ui import View, Button

class Useful(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
    
    async def searcher(self, inter, theme):
        Parser().search(theme)
        with open(config.result_path, 'r') as res:
            result = json.loads(res.read())['results']
            print(random.choice(result)['itemurl'])
            await inter.send(random.choice(result)['itemurl'])

    @commands.command(
        name='cat',
        options=[]
    )

    async def cat(self, inter:ApplicationCommandInteraction):
        await inter.message.delete()
        await self.searcher(inter, 'cat')
    
    @commands.command(
        name='dog',
        options=[]
    )

    async def dog(self, inter:ApplicationCommandInteraction):
        await inter.message.delete()
        await self.searcher(inter, 'dog')
        
    @commands.command(
        name='gif',
        options=[
            disnake.Option(
                name='search',
                description='Рандомная гифка по поиску',
                type=disnake.OptionType.string,
                required=True
            )
        ]
    )

    async def gif(self, inter:disnake.ApplicationCommandInteraction, search: str):
        await inter.message.delete()
        await self.searcher(inter, search)

    @commands.command(
        name='bear',
        options=[]
    )

    async def bear(self, inter:disnake.ApplicationCommandInteraction):
        await inter.message.delete()
        await self.searcher(inter, 'bear')

    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(
        name='set_timer',
        description='Устанавливает таймер',
        options=[
            Option(
                name='long',
                description='Насколько долго',
                type=OptionType.string,
                required=True,
            ),
            Option(
                name='name',
                description='Название таймера',
                type=OptionType.string,
                required=False
            )
        ]
    )
       
    async def set_timer(self, inter: commands.Context, long:str, name:str = ''):
        await inter.message.delete()
        t = getseconds(long)
        if t:
            if inter.guild.owner_id != inter.author.id:
                await inter.author.add_roles(inter.guild.get_role(config.timer_role_id))
            await inter.send(
                embed=YesNoEmbed(
                    f'Таймер {name} сработает через {long}',
                    True
                ).GetEmbed()
            )
            emb = EmbedHandler(title=f'Время вышло', description=f'Таймер {name} сработал', color=Colour.red())
            await asyncio.sleep(t)
            await self.searcher(inter=inter, theme='time is up')
            await inter.send(
                embed=emb.GetEmbed()
            )
            await inter.send(inter.author.mention)
            if inter.guild.owner_id != inter.author.id:
                await inter.author.remove_roles(inter.guild.get_role(config.timer_role_id))
        else:
            raise commands.BadArgument()

    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(read_message_history=True)
    @commands.bot_has_permissions(read_message_history=True)
    @commands.command(
        name='set_reaction',
        description='Добавить реакцию на выбранное сообщение',
        options=[
            Option(
                name='message_id',
                description='Id сообщения',
                type=OptionType.integer,
                required=True
            ),
            Option(
                name='reaction',
                description='Реакция, которую нужно добавить',
                type=OptionType.string,
                required=True
            )
        ]
    )
    async def set_reaction(self, inter: commands.Context, message_id: int, reaction: str):
        await inter.message.delete()
        for i in await inter.history().flatten():
            if i.id == message_id:
                await i.add_reaction(reaction)
                break

    @commands.command()
    async def bug_report(self, inter: commands.Context):
        overwrites = { 
            inter.guild.default_role: PermissionOverwrite(view_channel=False),
            inter.guild.get_role(config.reporter): PermissionOverwrite(view_channel=True, send_messages=True),
            inter.me.top_role: PermissionOverwrite(view_channel=True, send_messages=True),
        }
        await inter.author.add_roles(inter.guild.get_role(config.reporter))
        ch = await inter.guild.create_text_channel('bug-report', overwrites=overwrites)
        await ch.send(
            embed=EmbedHandler(title='Опишите баг и прикрепите все необходимые файлы подтверждающие наличие бага', description='Как напишете всё введите `!done`').GetEmbed()
        )
        data = []
        while True:
            u = 0
            for i in await ch.history().flatten():
                if i.content == '!done':
                    u = 1
                    break
                elif i not in data:
                    data.append(i)
            if u:
                break
        await ch.delete()
        await inter.author.remove_roles(inter.guild.get_role(config.reporter))
        text = ''
        ch = inter.guild.get_channel(config.bug_reports_chat)
        count = 1
        for i in data:
            i: Message
            for j in i.attachments:
                j: Attachment
                file = await j.to_file()
                await ch.send(file=file)
                count += 1
            text += i.content + '\n'
        emb = EmbedHandler(title='Bug reported', description=text)
        msg = await ch.send(
            embed=emb.GetEmbed()
        )
        v = View()
        v.add_item(Button(label='Решено!'))
        await ch.send(
            view=v
        ) 
        def check(inter):
            return inter
        ctx:MessageInteraction = await self.bot.wait_for('button_click', check=check)
        if ctx.component.label:
            dm = await inter.author.create_dm()
            await dm.send(
                embed=YesNoEmbed(
                    'Баг был исправлен!',
                    False
                ).GetEmbed()
            )
        data = await ctx.channel.history().flatten()
        for i in range(0, count):
            data[i].delete()

    @commands.command()
    async def spam(self, inter: commands.Context, text: str, count: int = 100):
        for _ in range(count):
            await inter.send(text)


def setup(bot):
    bot.add_cog(Useful(bot))