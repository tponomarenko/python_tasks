import os
import requests


host_url = "https://wttr.in/"
city_name = os.getenv("CITY", default="Chernihiv")
language = os.getenv("LANG", default="uk")

response = requests.get(
    f"{host_url}{city_name}",
    headers={"Accept-Language": language}
)

if response.status_code != 200:
    print("error occured")
else:
    print(response.text)
