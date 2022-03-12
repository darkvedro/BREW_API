import pytest
from methods import DOGMethods

@pytest.fixture(params=DOGMethods.get_all_breeds())
def breed_list(request):
    return request.param