#!/usr/bin/env python3
import sys
import requests
import json
#import pandas as pd
import re
import datetime as dt
from time import sleep

#my_branch 

class Scraper:
    def __init__(self):
        pass

    def request(self):
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

        response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes', headers=headers, params=params)

        response = json.loads(response.text)

        return response

    def process(self):
        pass

    def run(self):
        self.response = self.request()
        return self.response

    def output_to_a_file(self, file_name:str):
        standard_stdout = sys.stdout
        new_output_file = open(file_name, 'w')
        sys.stdout = new_output_file

        #print(self.run())

        print(self.run()['Results'])

        sys.stdout = standard_stdout
        new_output_file.close()

scraper = Scraper()

results = scraper.run()['Results']

for result in results:
    print(result['Make_ID'])

for result in results:
    print(result['Make_Name'])






    




