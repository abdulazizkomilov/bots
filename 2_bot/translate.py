import requests
from pprint import pprint as print


app_id = "'f42a879e'"
app_key = "2dcf1c6c77083320619da4f37f85e50e"

language = "en-gb"
word_id = "python"

url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": 'f42a879e', "app_key": '2dcf1c6c77083320619da4f37f85e50e'})
print(r.status_code)
# res = r.json()
# print(res)