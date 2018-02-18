import requests

article = 'Edison'
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=categories&cllimit=100&format=json&plnamespace=0&formatversion=2&titles=' + article

r = requests.get(url)
js = r.json()

for cat in js["query"]["pages"][0]["categories"]:
    print(cat['title'])

print (js[0][0])

print(r.json())