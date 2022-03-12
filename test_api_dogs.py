import pytest
import requests
from methods import DOGMethods


class TestDog:

    def test_K1(self):
        assert len(DOGMethods.get_all_breeds()) == 95

    def test_K2(self):
        response = (requests.get('https://dog.ceo/api/breeds/list/all'))
        assert response.headers['Content-Type'] == 'application/json'

    def test_K3(self):
        response = requests.get('https://dog.ceo/api/breeds/list/all').json()
        assert response['status'] == 'success'

    @pytest.mark.parametrize('breed_list', DOGMethods.get_all_breeds())
    def test_K4(self, breed_list):
        response = DOGMethods.request_image(breed_list)
        assert response.status_code == 200

    def test_K5(self, breed_list):
        response = DOGMethods.request_image(breed_list)
        assert response.json()['message'] is not None