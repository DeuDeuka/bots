import random
from tools.parser import Parser
import config, json

class Searcher:
    def __init__(self):
        self.parser = Parser()
        
    async def send(self, inter, theme):
        self.parser.search(theme)
        with open(config.result_path, 'r') as res:
            result = json.loads(res.read())['results']
            await inter.send(random.choice(result)['itemurl'])
    