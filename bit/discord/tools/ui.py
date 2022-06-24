from typing import List, Optional
import disnake
from disnake.ext import commands
from disnake.ui import Select, View


class Select(disnake.ui.Select):
    def __init__(self, view, placeholder: str = '', max_values: int = 1, min_values: int = 1, options: List[disnake.SelectOption] = []):
        self.view = view
        super().__init__(placeholder=placeholder,max_values=max_values,min_values=min_values,options=options)

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.send_message(self.values[0])


class SelectView(disnake.ui.View):
    def __init__(self, *, timeout = 180, placeholder: str = '', max_values: int = 1, min_values: int = 1, options: List[disnake.SelectOption] = []):
        super().__init__(timeout=timeout)
        self.add_item(Select(self, placeholder=placeholder,max_values=max_values,min_values=min_values,options=options))

class View(disnake.ui.View):
    def __init__(self, *, timeout: Optional[float] = 180):
        super().__init__(timeout=timeout)