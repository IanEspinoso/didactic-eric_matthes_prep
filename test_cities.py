from city_functions import city_country

def test_city_country():
    """Test city functions without 'population'."""

    city_country_1 = city_country('santiago', 'chile')
    assert city_country_1 == 'Santiago, Chile'

def test_city_country_population():
    """Test city functions with all the arguments."""

    city_country_1 = city_country('santiago', 'chile', population='5000000')
    assert city_country_1 == 'Santiago, Chile - population 5000000'