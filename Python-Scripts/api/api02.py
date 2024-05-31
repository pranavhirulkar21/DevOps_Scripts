import requests
"""
payload = {'page': 2, 'count': 25}
responce = requests.get('https://httpbin.org/get', params=payload)

#print(responce.text)
print(responce.url)
"""

payload = {'uername': 'John', 'password': 'abc123'}
res = requests.post('https://httpbin.org/post', data=payload)

#print(res.text)
#print(res.json())

res_dict = res.json()
print(res_dict['form'])