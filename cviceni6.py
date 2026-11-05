import sys
import requests
import json

url = 'https://www.jcu.cz/cz/'
url1 = 'https://data.carnewschina.com/suggest?q='
url2 = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'


def get_model_names(prefix):
    models = []

    try:
        response = requests.get(url1 + prefix)

        if response.status_code == 200:
            data = response.json()

            for model in data["models"]:
                models.append(model["name"])

    except Exception as e:
        print(f"Chyba: {e}")

    return models

def download_rates():
    kurzy = {}

    response = requests.get(url2)

    if response.status_code == 200:
        lines = response.text.splitlines()

        for line in lines[2:]:
            parts = line.split("|")

            if len(parts) != 5:
                print("chyba spatny format dat")
            else:
                mena = parts[3]
                hodnota = int(parts[2])
                kurz = float(parts[4].replace(",", "."))

                kurzy[mena] = kurz / hodnota

    return kurzy


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} prefix")
        sys.exit()

    prefix = sys.argv[1]
    models = get_model_names(prefix)
    for model in models:
        print(model)

    rates = download_rates()

    for mena, kurz in rates.items():
        print(mena, kurz)