def format_city_country(city, country, population=None):
    formatted = f"{city.title()}, {country.title()}"
    if population is not None:
        formatted += f' - population {population}'
    return formatted

