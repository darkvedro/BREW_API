
import requests

class BMethods:

    @staticmethod
    def get_all_breweries_id():
        response = requests.get('https://api.openbrewerydb.org/breweries').json()
        breweries_id = []
        for item in response:
            breweries_id.append(item['id'])
        return breweries_id

    @staticmethod
    def get_all_breweries_name():
        response = requests.get('https://api.openbrewerydb.org/breweries').json()
        breweries_name = []
        for item in response:
            breweries_name.append(item['name'])
        return breweries_name

    @staticmethod
    def request_brewery_information(brewery_id):
        response = requests.get('https://api.openbrewerydb.org/breweries/' + str(brewery_id))
        return response