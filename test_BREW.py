import pytest
import requests
from methods import BMethods

class Testbreew:

    def test_B1(self):
        response = requests.get('https://api.openbrewerydb.org/breweries').json()
        assert len(response) == 20

    def test_B2(self, state):
        response = requests.get('https://api.openbrewerydb.org/breweries?by_state=' + state)
        assert response.status_code == 200
        assert response.json()[0]["state"] == state

    def test_B3(self, brewery_name):
        response = requests.get("https://api.openbrewerydb.org/breweries?by_name=" + brewery_name)
        assert response.status_code == 200
        assert brewery_name in response.json()[0]["name"]

    def test_B4(self, brewery_id):
        response = BMethods.request_brewery_information(brewery_id)
        assert response.status_code == 200
        assert response.json()["id"] == brewery_id

    @pytest.mark.parametrize('ids_param', BMethods.get_all_breweries_id())
    def test_B(self, ids_param):
        response = requests.get('https://api.openbrewerydb.org/breweries/' + str(ids_param))
        assert response.status_code == 200
        assert response.json()["id"] == ids_param