import requests
from flight_search import FlightSearch

# {'price': {'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54}}
SHEETY_END_POINT = "https://api.sheety.co/3461b4c69feeced3d329745da58320cb/flightDeals/prices/"
fs = FlightSearch()


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHEETY_END_POINT)
        response.raise_for_status()
        self.sheet_data = response.json()
        return self.sheet_data

    def update_city_code(self):

        for row in self.sheet_data['prices']:
            if (row['iataCode']) == '':
                sheety_put_url = f"{SHEETY_END_POINT}/{row['id']}"
                city = row['city']
                new_data = {
                    "price": {
                        "iataCode": fs.get_destination_code(city)
                    }
                }
                put_response = requests.put(url=sheety_put_url, json=new_data)
                print(put_response.text)
