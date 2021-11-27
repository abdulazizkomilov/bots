import requests
from pprint import pprint as print

API_KEY = '3f220948906c87f9d3642fe9'

currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
# print(response.status_code)
# print(response.json())
kurs = response.json()['conversion_rate']
print(f"Bugungi kurs: 1AQSH dollori {kurs}")