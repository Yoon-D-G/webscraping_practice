from json import JSONDecodeError

import requests
import json
import pandas as pd
from time import sleep, time
import pickle as pickle


class Scraper:
    class Cache:
        def __init__(self, persist):
            self.__persist__ = persist
            self.__inner_cache__ = {}
            if self.__persist__:
                self.__inner_cache__ = self.__deserialize__()

        def __serialize__(self):
            with open(".cache", "wb") as cached_dictionary:
                pickle.dump(self.__inner_cache__, file=cached_dictionary)

        def __deserialize__(self):
            try:
                with open(".cache", "rb") as cached_dictionary:
                    try:
                        return pickle.load(file=cached_dictionary)
                    except EOFError:
                        return {}
            except FileNotFoundError:
                with open(".cache", "xb"):
                    return {}

        def cache_value(self, key, value):
            if key in self.__inner_cache__:
                return self.__inner_cache__[key]
            self.__inner_cache__[key] = value

            if self.__persist__:
                self.__serialize__()

            return value

        def get_value(self, key):
            return self.__inner_cache__[key]

        def get_cache(self):
            if self.__inner_cache__:
                return self.__inner_cache__
            else:
                return {}

    def __init__(self):
        self.cache = self.Cache(True)

    def request(self, endpoint, retry_limit, timeout, cache):
        time_start = time()
        if endpoint in self.cache.get_cache():
            time_end = time()
            print(f"Cached request took {round(time_end - time_start, 5)}s for endpoint: {endpoint}")
            return self.cache.get_value(endpoint)

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

        response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/{}'.format(endpoint), headers=headers,
                                params=params)
        time_end = time()
        print(f"Request took {round(time_end - time_start, 5)}s for endpoint: {endpoint}")

        if response.status_code != 200:
            if retry_limit != 0:
                sleep(timeout)
                return self.request(endpoint, retry_limit - 1, timeout, False)
            else:
                return {}
        try:
            json_string = json.loads(response.text)['Results']
            if json_string and cache:
                self.cache.cache_value(endpoint, json_string)
            return json_string
        except JSONDecodeError as ex:
            return {}

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
        return output

    def get_makes(self):
        return self.request(endpoint='getallmakes', retry_limit=2, timeout=2, cache=False)

    def get_models(self, make_value: str):
        return self.request(endpoint='getmodelsformake/{}'.format(make_value), retry_limit=2, timeout=2, cache=True)


if __name__ == '__main__':
    scraper = Scraper()
    all_makes = scraper.get_makes()
    for make in all_makes:
        print(pd.DataFrame(scraper.get_models(make['Make_Name'])))
