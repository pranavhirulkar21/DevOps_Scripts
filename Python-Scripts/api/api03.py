import requests

r = requests.get('https://httpbin.org/basic-auth/john/abc123', auth=('john', 'abc123'))

print(r)
#print(r.text)

rr = requests.get('https://httpbin.org/delay/1', timeout=5)
print(rr)