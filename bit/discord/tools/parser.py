import random
import requests
import config, json
from disnake.ext.commands import ObjectNotFound

class Parser():
    def __init__(self):
        self.apikey = 'LIVDSRZULELA'
        self.lmt = 10

    def search(self, search_term):

        r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, self.apikey, self.lmt))

        if r.status_code == 200:
            with open('database/result.json', 'w') as res:
                json.dump(json.loads(r.content), res)
        else:
            raise ObjectNotFound

