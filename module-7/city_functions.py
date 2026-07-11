# Name: Peter Ddamulira
# Assignment: Module 7.2 - Test Cases
# Description:
# This program defines a function that formats a city and country
# into one readable string.

# Name: Peter Ddamulira
# Assignment: Module 7.2 - Test Cases

def city_country(city, country, population=None, language=None):
    location = f"{city.title()}, {country.title()}"

    if population is not None:
        location += f" - population {population}"

    if language is not None:
        location += f", {language.title()}"

    return location


print(city_country("Santiago", "Chile"))
print(city_country("Kampala", "Uganda", 1680600))
print(city_country("Dallas", "United States", 1300000, "English"))