import requests

url = "https://api.chucknorris.io/"
response = requests.get(url)
vitsit = response
for vitsi in vitsit():
    print(f"{vitsi['value']}")