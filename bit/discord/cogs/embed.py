from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands
from tools.searcher import Searcher
from disnake.ui import *
from tools.EmbedHandler import EmbedHandler

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='embed',
        description='Создаёт embed по указанным параметрам',
        options=[
            Option(
                name='title',
                description='Заголовок',
                type=OptionType.string,
                required=False,
            ),
            Option(
                name='description',
                description='Описание',
                type=OptionType.string,
                required=False,
            ),
            Option(
                name='field_title',
                description='Заголовок дополнительного поля',
                type=OptionType.string,
                required=False,
            ),
            Option(
                name='field_desctiption',
                description='Описание дополнительного поля',
                type=OptionType.string,
                required=False,
            ),
            Option(
                name='inline',
                description='В одну строку',
                type=OptionType.boolean,
                required=False,
            ),
            Option(
                name='footer_text',
                description='Текса "подвала"',
                type=OptionType.string,
                required=False,
            ),
            Option(
                name='footer_icon',
                description='Url иконки "подвала"',
                type=OptionType.string,
                required=False,
            ),
            Option(
                name='image',
                description='Url изображения',
                type=OptionType.string,
                required=False,
            ),
            Option(
                name='gif',
                description='Название гифки',
                type=OptionType.string,
                required=False,
            ),
        ]
    )
    async def embed(self, inter:ApplicationCommandInteraction, title = '', description = '', field_title = '', field_desctiption = '', inline = True, footer_text = '', footer_icon = '', image = '', gif = ''):
        await inter.message.delete()
        emb = EmbedHandler(title=title, description=description, color=inter.author.top_role.color)
        emb.SetAuthor(author=inter.author, icon=inter.author.avatar.url)
        if field_title and field_desctiption:
            emb.AddField(title=field_title, description=field_desctiption, inline=inline)
        if footer_text or footer_icon:
            emb.SetFooter(text=footer_text, icon=footer_icon)
        if image:
            emb.SetImage(url=image)
        if gif:
            self.searcher.send(inter, gif)
        await inter.send(
            embed=emb.GetEmbed()
        )

def setup(bot):
    bot.add_cog(Embed(bot))