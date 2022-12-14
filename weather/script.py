import os
import requests


host_url = "https://wttr.in/"
city_name = os.getenv("CITY", default="Chernihiv")
response = requests.get(f"{host_url}{city_name}")
if response.status_code != 200:
    print("error occured")
else:
    print(response.text)
