import disnake
from disnake.ext import commands
from disnake.ui import View, Button
from config import mafia
from tools.EmbedHandler import YesNoEmbed

class Mafia(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
    
    @commands.bot_has_permissions(manage_roles=True, manage_channels=True)
    @commands.command(
        name='mafia'
    )
    async def maifa(self, ctx: commands.Context):
        print('mafia')
        m = mafia()
        v = View()
        v.add_item(Button(label='Обычный'))
        v.add_item(Button(label='Экстра'))
        mafia_player: dict
        await ctx.send(view=v)

        def check(inter):
            return inter

        inter: disnake.MessageInteraction = await self.bot.wait_for('button_click', check=check)
        if inter.author.id == ctx.author.id:
            mafia_players = m.mafia_players[inter.component.label]
            await inter.send(
                embed=YesNoEmbed(
                    f'Выбран режим: {inter.component.label}',
                    True
                ).GetEmbed()
            )
            v = View(timeout=None)
            role = await ctx.guild.create_role(name='mafia')
            overwrites = {
                disnake.utils.get(ctx.guild.roles, name = '@everyone'): disnake.PermissionOverwrite(view_channel=False),
                role: disnake.PermissionOverwrite(view_channel=True),
                disnake.utils.get(ctx.guild.roles, name = 'botik'): disnake.PermissionOverwrite(view_channel=True),
            }
            ch = await ctx.guild.create_text_channel(name='Mafia_game', overwrites=overwrites)
            v.add_item(Button(label='Присоединиться к игре'))
            await ctx.send(view=v)
            inter = await self.bot.wait_for('button_click', check=check)
            await inter.author.add_roles(role)
            await ch.send(
                embed=YesNoEmbed(
                    inter.author.mention + f' присоединился к игре',
                    True
                ).GetEmbed()
            )
        else:
            await inter.send(
                embed=YesNoEmbed(
                    f'Не ты начинаешь игру',
                    False
                ).GetEmbed(),
                ephemeral=True
            )


def setup(bot):
    bot.add_cog(Mafia(bot))