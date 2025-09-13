def city_country(city, country, population=''):
    """Pretty prints a given city, country and population."""

    if population != '':
        population = f" - population {population}"
    return f"{city.capitalize()}, {country.capitalize()}{population}"