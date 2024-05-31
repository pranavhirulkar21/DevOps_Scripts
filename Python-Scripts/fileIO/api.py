import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as responce:
    source = responce.read()
    
data = json.loads(source)
    
#print(json.dumps(data, indent=2))

for item in data['list']['resources']:
    print(item)
    """
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price
    
print(usd_rates['USD/EUR'])
"""