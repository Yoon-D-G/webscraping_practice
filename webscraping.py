import requests
import json
import pandas as pd
import re
import datetime as dt
from time import sleep

class Scraper:
    def __init__(self):
        pass 
    
    def request(self, endpoint):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Referer': 'https://vpic.nhtsa.dot.gov/api/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }

        params = (
            ('format', 'json'),
        )

        response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/{}'.format(endpoint), headers=headers, params=params)

        response = json.loads(response.text)

        return response['Results']

    def process(self, results: list):
        output = ''
        for result in results:
            output += self.format_line(result) + '\n'
            # print(output)
        return output

    def run(self):
        all_makes = self.request('getallmakes')
        # print(all_makes)
        output = ''
        counter = 0
        for make in all_makes:
            if counter == 5:
                break
            output += str(self.process(self.request('getmodelsformake/{}'.format(make['Make_Name']))))
            counter += 1

        return output

    def format_line(self, list):
        return 'ID:{id} Make:{make}'.format(id=list['Make_ID'], make=list['Make_Name'])

scraper = Scraper()
print(scraper.run())



