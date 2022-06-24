from enum import Flag
import re
import config
import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Guild, Member, PartialEmoji, Role, Option, OptionType, Embed, RawReactionActionEvent, Message
from tools.EmbedHandler import EmbedHandler, YesNoEmbed

class UserActivity(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(
        name='add_role',
        description='',
        options=[
            Option(
                name='role',
                description='',
                type=OptionType.role,
                required=True,
            ),
            Option(
                name='member',
                description='',
                type = OptionType.user,
                required=False,
            )
        ]
    )

    async def add_role(self, inter, role: Role, member: Member = None):
        await inter.message.delete()
        if member:
            if role in member.roles:
                await inter.send(embed=Embed(title=f'Role already on {member.name.mention}!'))
                return
            await member.add_roles(role)
            await inter.send(embed=Embed(title='Role added!'))
        else:
            member = inter.author
            if role in member.roles:
                await inter.send(embed=Embed(title=f'Role already on you!'))
                return
            await member.add_roles(role)
            await inter.send(embed=Embed(title='Role added!'))
    
    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(
        name='new_role',
        description='Создаёт роль на сервере',
        options=[
            Option(
                name='name',
                description='Название роли',
                type=OptionType.string,
                required=True
            ),
            Option(
                name='descent',
                description='Наследование всех разрешений от роли',
                type=OptionType.role,
                required=False
            )
        ]
    )

    async def new_role(self, inter: ApplicationCommandInteraction, name: str, descent: Role = ''):
        await inter.message.delete()
        if descent:
            role = await inter.guild.create_role(name=name, permissions=descent.permissions, hoist=descent.hoist, colour=descent._colour)
        else:
            role = await inter.guild.create_role(name=name)

        await inter.send(
            embed=YesNoEmbed(
                f'Роль {role.mention} создана',
                True
            ).GetEmbed()
        )
    
    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(
        name='delete_role',
        description='Удаляет роль на сервере',
        options=[
            Option(
                name='name',
                description='Название роли',
                type=OptionType.role,
                required=False
            )
        ]
    )

    async def delete_role(self, inter: ApplicationCommandInteraction, name: Role):
        await inter.message.delete()
        if name.id not in inter.me.roles:
            await name.delete()
            await inter.send(
                embed=YesNoEmbed(
                    f'Роль {name.name} удалена',
                    True
                ).GetEmbed()
            )
        else:
            await inter.send(
                embed=YesNoEmbed(
                    f'Нельзя удалить роль бота',
                    False
                ).GetEmbed()
            )

    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(
        name='remove_role',
        description='',
        options=[
            Option(
                name='role',
                description='',
                type=OptionType.role,
                required=True,
            ),
            Option(
                name='member',
                description='',
                type = OptionType.user,
                required=False,
            )
        ]
    )

    async def remove_role(self, inter, role: Role, member: Member = None):
        await inter.message.delete()
        if member:
            if role not in member.roles:
                await inter.send(embed=Embed(title=f'Роли не было на {member.name.mention}!'))
                return
            await member.remove_roles(role)
            await inter.send(embed=Embed(title='Роль удалена!'))
        else:
            member = inter.author
            if role not in member.roles:
                await inter.send(embed=Embed(title=f'Роль не найдена'))
                return
            await member.remove_roles(role)
            await inter.send(embed=Embed(title='Роль удалена'))

    @commands.has_role(config.owner_role_id)
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    @commands.command(
        name='edit_nickname',
        description='',
        options=[
            Option(
                name='new_nick',
                description='',
                type=OptionType.string,
                required=True,
            ),
            Option(
                name='member',
                description='',
                type=OptionType.user,
                required=False,
            )
        ]
    )

    async def edit_nickname(self, inter, new_nick: str, member: Member = None):
        await inter.message.delete()
        if not member:
            member = inter.author
        try:
            await member.edit(nick=new_nick)
            await inter.send(
                embed=YesNoEmbed(
                    '`Изменено!`',
                    True
                ).GetEmbed()
            )
        except:
            await inter.send(
                embed=YesNoEmbed(
                    '`Я не могу сделать это..`',
                    False
                ).GetEmbed()
            )

def setup(bot):
    bot.add_cog(UserActivity(bot))
