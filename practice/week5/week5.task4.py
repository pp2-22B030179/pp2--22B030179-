def cities_starting_with_letter(city_list, letter):
    """
    Yields cities from the given list whose names start with the given letter.
    """
    for city in city_list:
        if city.startswith(letter):
            yield city
cities = ["Astana", "Almaty", "Karagandy", "Pavlodar", "Kostanai", "Semey"] 
letter = 'K'

for city in cities_starting_with_letter(cities, letter):
    print(city)