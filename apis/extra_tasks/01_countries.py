'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
import requests

base_url = "https://restcountries.com/v3.1/"

home_country = "Uganda"
home_country_info = f"{base_url}name/{home_country}"

response_home = requests.get(home_country_info)
home_data = response_home.json()[0] if response_home.ok else None

current_country = "Kenya"
current_country_info = f"{base_url}name/{current_country}"

response_current = requests.get(current_country_info)
current_data = response_current.json()[0] if response_current.ok else None

if home_data and current_data:
    if current_data["population"] > home_data["population"]:
        print(f"{current_country} has a larger population")
    elif current_data["population"] < home_data["population"]:
        print(f"{home_country} has a larger population")
    else:
        print(f"{current_country} and {home_country} have the same population")

    if current_data["area"] > home_data["area"]:
        country_area = current_data["area"] - home_data["area"]
        print(f"{current_country} is larger in size than {home_country} by {country_area} square kilometers")
    elif current_data["area"] < home_data["area"]:
        country_area = home_data["area"] - current_data["area"]
        print(f"{home_country} is larger in size than {current_country} by {country_area} square kilometers")
    else:
        print(f"{current_country} and {home_country} have the same area")

    print(f"Native name of {home_country} is {home_data.get('nativeName')}")
    print(f"Native name of {current_country} is {current_data.get('nativeName')}")
else:
    print("Failed to retrieve country information.")

