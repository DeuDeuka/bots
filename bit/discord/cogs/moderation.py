import config
import disnake
import asyncio
from disnake.ext import commands
from datetime import timedelta
from disnake import ApplicationCommandInteraction, Guild, Option, OptionType, Member
from tools.getseconds import getseconds
from tools.EmbedHandler import YesNoEmbed

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.command(
        name='kick',
        description='Выгнать участника',
        option=[
            Option(
                name='member',
                description='Кто должен покинуть сервер',
                type=OptionType.user,
                required=True
            ),
            Option(
                name='reason',
                description='Причина',
                type=OptionType.string,
                required=False,
            )
        ]
    )
    async def kick(self, inter, member: Member, reason: str = 'Просто так)'):
        await inter.message.delete()
        if member.id == inter.author.id:
            await inter.send(
                embed=YesNoEmbed('Вы не можете кикнуть себя!', False).GetEmbed()
            )
            return
        
        await inter.send(f'{member.name} выгнан по причине: {reason}')
        await member.kick(reason=reason)


    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command(
        name='ban',
        description='Заблокировать пользователя',
        option=[
            Option(
                name='member',
                description='Кто должен быть заблокирован',
                type=OptionType.user,
                required=True
            ),
            Option(
                name='reason',
                description='Причина',
                type=OptionType.string,
                required=False,
            ),
            Option(
                name='time',
                description='Время блокировки',
                type=OptionType.string,
                required=False,
            )
        ]
    ) 
    async def ban(self, inter, member:Member, reason: str = 'Потому что)', time: str = '111y'):
        await inter.message.delete()
        if not getseconds(time):
            await inter.send(
                embed = YesNoEmbed('Введите правильное время', False).GetEmbed()
            )
            return
        if member.id == inter.author.id:
            await inter.send(
                embed = YesNoEmbed('Нельзя заблокировать самого себя', False).GetEmbed()
            )
            return
        
        await inter.send(
            embed=YesNoEmbed(f"{member.mention} was banned blyat' bc {reason}", True).GetEmbed()
        )
        await member.ban(reason=reason)

        await asyncio.sleep(getseconds(time))
        await member.unban(reason='time is up')
        await inter.send(
            embed = YesNoEmbed(f"Пользователь {member.name} разблокирован", True).GetEmbed()
        )

    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.command(
        name='clear',
        description='clear',
        options=[
            Option(
                name='count',
                description='count',
                type=OptionType.integer,
                required = False
            ),
        ]
        )
    async def clear(self, inter, count: int = 500):
        await inter.message.delete()
        if not (1 <= count <= 500):
            await inter.send(
                embed=YesNoEmbed(
                    'Не в пределах от 1 до 500',
                    False
                ).GetEmbed()
            )
            return

        await inter.send(
                embed=YesNoEmbed(
                    'Готово!',
                    True
                ).GetEmbed()
            )
        await inter.channel.purge(limit=count)

def setup(bot):
    bot.add_cog(Moderator(bot))