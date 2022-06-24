import typing
from disnake import Color, Colour, Embed
import disnake

class EmbedHandler:
    def __init__(self, title: str = '', description: str = '', color: Colour = Color.blurple()):
        self.embed = Embed(title=title, description=description, color=color)
    
    def GetEmbed(self):
        return self.embed

    def SetAuthor(self, author: str = '', icon: str = '', url: str = ''):
        self.embed = self.embed.set_author(name=author, icon_url=icon, url=url)
    
    def AddField(self, title: str = '', description: str = '', inline: bool = True):
        self.embed = self.embed.add_field(name=title, value=description, inline=inline)

    def SetFooter(self, text: str = '', icon: str = ''):
        self.embed = self.embed.set_footer(text=text, icon_url=icon)

    def RemoveAuthor(self, author: str = '', icon: str = '', url: str = '#'):
        self.embed = self.embed.remove_author()
    
    def RemoveField(self):
        self.embed = self.embed.remove_field()

    def RemoveFooter(self):
        self.embed = self.embed.remove_footer()
        
    def FromDict(self, dict: dict):
        self.embed = self.embed.from_dict(dict)

    def SetImage(self, url):
        self.embed = self.embed.set_image(url=url)
    
    def SetThumbnail(self, url):
        self.embed = self.embed.set_thumbnail(url=url)
    
class YesNoEmbed:
    def __init__(self, text: str, bool: bool):
        if bool:
            self.embed = Embed(
                title='Готово',
                description=text,
                color=Colour.brand_green()
            )
        else:
            self.embed = Embed(
                title='Ошибка',
                description=text,
                color=Colour.brand_red()
            )
    def GetEmbed(self):
        return self.embed