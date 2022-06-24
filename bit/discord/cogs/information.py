import json
import random
from turtle import color
import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Option, OptionType, Embed, Member
import config
from tools.EmbedHandler import EmbedHandler
from tools.searcher import Searcher

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.searcher = Searcher()

    @commands.command(
        name='user_info',
        description='',
        options=[
            Option(
                name='member',
                description='Member info',
                type=OptionType.user,
                required=False
            )
        ]
    )
    
    async def user_info(self, inter:ApplicationCommandInteraction, member: Member = None):
        await inter.message.delete()
        if member:
            info_embed = EmbedHandler(
                title=f'Info about {member.name}',
                color=member.top_role.colour
            )

            info_embed.AddField(
                'Date of registration:',
                f'<t:{int(member.created_at.timestamp())}>',
                inline=False
            )
            info_embed.AddField(
                'Status:', 
                member.desktop_status,
                inline=False
            )
            info_embed.AddField(
                'Date of joining server:', 
                f"<t:{int(member.joined_at.timestamp())}>",
                inline=False
            )
            info_embed.AddField(
                'Role:',
                member.top_role.mention,
                inline=False
            )

        else:
            info_embed = EmbedHandler(
                title=f'Info about {inter.author.name}',
                color=inter.author.top_role.colour
            )

            info_embed.AddField(
                'Date of registration:',
                f'<t:{int(inter.author.created_at.timestamp())}>',
                inline=False
            )
            info_embed.AddField(
                'Status:', 
                inter.author.desktop_status,
                inline=False
            )
            info_embed.AddField(
                'Date of joining server:', 
                f"<t:{int(inter.author.joined_at.timestamp())}>",
                inline=False
            )
            info_embed.AddField(
                'Role:',
                inter.author.top_role.mention,
                inline=False
            )

        await self.searcher.send(inter, 'Server member')
        await inter.send(embed=info_embed.GetEmbed())

    @commands.command(
        name='guild_info',
        description='Server info',
        options=[]
    )
    
    async def guild_info(self, inter):
        await inter.message.delete()
        info_embed = EmbedHandler(
            title=f'{inter.guild.name} info:'
        )
        info_embed.AddField(
            '`Date of creation:`',
            f'<t:{int(inter.guild.created_at.timestamp())}>',
            inline=False
        )
        info_embed.AddField(
            '`Count of members^`', 
            f'{inter.guild.member_count}',
            inline=False
        )
        info_embed.AddField(
            '`Creator:`', 
            f'{inter.guild.owner}',
            inline=False
        )
        info_embed.AddField(
            '`Stickers count:`',
            f'{len(inter.guild.stickers)}',
            inline=False
        )
        await self.searcher.send(inter, 'Server')
        await inter.send(embed=info_embed.GetEmbed())

def setup(bot):
    bot.add_cog(Information(bot))