from disnake.ui import View, Button
from disnake.ext import commands
import disnake
from disnake import MessageInteraction
from tools.modal import MyModal

class UI(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def test(self, ctx: commands.Context):
        def check(inter):
            return inter

        v = View()
        b = Button(label='Test', custom_id='test')
        b1 = Button(label='Test1', custom_id='test1')
        v.add_item(b)
        v.add_item(b1)
        await ctx.send(view=v)
        inter: disnake.MessageInteraction = await self.bot.wait_for('button_click', check=check)
        await inter.response.send_message(inter.message.content, ephemeral=True)
    
    @commands.command()
    async def modaltest(self, ctx: commands.Context):
        def check(inter):
            return inter
        v = View()
        v.add_item(Button(label='Modal'))
        await ctx.send(view=v)
        inter:MessageInteraction = await self.bot.wait_for('button_click', check=check)
        await inter.response.send_modal(modal=MyModal())

def setup(bot):
    bot.add_cog(UI(bot))