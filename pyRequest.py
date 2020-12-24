import requests

f = requests.get("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")
print(f)
