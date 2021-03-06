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
        #protect this request
        #one scenario for 200 response (everything went fine)
        #a different scenario for any other request code (eg 404, 503) - 10 second cooldown before another request then try again.
        #try this 5 times and then give up and move on to the next request
        #extension - keep track of how many requests have failed in a row. If there is a certain threshold (eg 5 requests in a row)
        #then stop doing requests. persistent or non-persistent counter. 

        response = json.loads(response.text)

        return response['Results']

    def process(self, results: list):
        output = []
        for result in results:
            result_dict = {
                'Make': result.get('Make_Name'),
                'Model': result.get('Model_Name'),
                'Make ID': result.get('Make_ID'),
                'Model ID': result.get('Model_ID')
            }
            output.append(result_dict)
        output_df = pd.DataFrame(output)
        return output_df

    def run(self):
        all_makes = self.request('getallmakes')
        responses = []
        counter = 0
        for make in all_makes:
            if counter == 20:
                break
            response = self.request('getmodelsformake/{}'.format(make['Make_Name']))
            process_response = self.process(response)
            responses.append(process_response)
            counter += 1
        return responses

    def format_line(self, list):
        return 'ID:{id} Make:{make}'.format(id=list['Make_ID'], make=list['Make_Name'])

if __name__ == '__main__':
    scraper = Scraper()
    for response in scraper.run():
        print(response)





