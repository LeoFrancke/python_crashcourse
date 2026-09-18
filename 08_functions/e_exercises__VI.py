# 8.6 Exercise - City names

def city_country(city, country):
    """Return a formatted city-country pair."""
    return f"{city.title()}, {country.title()}"


br = city_country('campinas', 'brazil')
ru = city_country('st. petesburg', 'russia')
ca = city_country('ottawa', 'canada')
print(br)
print(ru)
print(ca)

