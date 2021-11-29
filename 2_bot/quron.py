import requests
from pprint import pprint as print

surah = 1
ayat = 4
tafsir = 'uzb-muhammadsodikmu'
language = 'ar'

url_sura = f"http://api.alquran.cloud/v1/edition/language/{language}"

response = requests.get(url_sura)
# print(response.status_code)
print(response.json())
# kurs = response.json()['conversion_rate']
print(response)