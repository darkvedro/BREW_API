
import pytest
from methods import BMethods

@pytest.fixture(params=['Dog', 'Beer', 'England'])
def brewery_name(request):
    return request.param

@pytest.fixture(params=BMethods.get_all_breweries_id())
def brewery_id(request):
    return request.param

@pytest.fixture(params=['Indiana', 'Oregon', 'Colorado',
                        'California', 'Nevada', 'Ohio'])
def state(request):
    return request.param