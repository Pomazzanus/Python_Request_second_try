import requests
import json


class CryptoData:
    def __init__(self, start_url):
        self.start_url = start_url

    def get_to_json(self):
        res = requests.get(self.start_url).json()
        to_json = json.dumps(res["data"]["cryptoCurrencyList"], indent=2)
        print(to_json)
        self.save_as_json(to_json)

    def save_as_json(self, to_json):
        file = open("crypto_data.json", "w")
        file.write(to_json)
        file.close()


if __name__ == "__main__":
    url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000&sortBy=market_' \
          'cap&%20sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24' \
          'h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_' \
          '30d,volume_60d'

    data_scraper = CryptoData(url)
    data_scraper.get_to_json()
