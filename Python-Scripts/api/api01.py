import requests

url = "https://xkcd.com/353/"
r1 = requests.get(url)

# you can directly write
# r = request.get('https://xkcd.com/353/')
# instead of line 3 and 4

print(r1)
#print(dir(r1))
#print(help(r1))
#print(r1.text) 


r2 = requests.get("https://imgs.xkcd.com/comics/python.png")
#print(r2.content)

with open('comic.png', 'wb') as f: #...wb = write-byte 
    f.write(r2.content)
    
   
r3 = requests.get("https://imgs.xkcd.com/comics/python.png")
print(r3.status_code)
print(r3.ok)
print(r3.headers) 
    