import requests


class DOGMethods:

    @staticmethod
    def request_image(breed_item):
        response = requests.get('https://dog.ceo/api/breed/' + breed_item + '/images/random')
        return response

    @staticmethod
    def get_all_breeds():
        response = requests.get('https://dog.ceo/api/breeds/list/all')
        all_breeds = list(response.json()['message'])
        return all_breeds
