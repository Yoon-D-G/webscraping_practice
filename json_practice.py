import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open('data_file.json', 'w', encoding='utf-8') as write_file:
    json.dump(data, write_file, ensure_ascii=False, indent=4)



