from city_functions import city_country

def test_city_country():
    """Test city_functions."""

    city_country_1 = city_country('santiago', 'chile')
    assert city_country_1 == 'Santiago, Chile'