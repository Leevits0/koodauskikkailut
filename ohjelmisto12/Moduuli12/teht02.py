import requests

def hae_säätiedot(paikkakunta, api_avain):
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}")
    response = requests.get(url)
    säätiedot = response.json()

    if response.status_code == 200:
        lämpötila_kelvin = säätiedot['main']['temp']
        lämpötila_celcius = lämpötila_kelvin - 273.15
        kuvaus = säätiedot['weather'][0]['description']
        return kuvaus, lämpötila_celcius
    else:
        print(f"Virhe: HTTP status code: {response.status_code}")
        return None, None

api_avain = input("Syötä API-avain: ")
paikkakunta = input("Syötä paikkakunta: ")

kuvaus, lämpötila = hae_säätiedot(paikkakunta,api_avain)

if kuvaus and lämpötila:
    print(f"Sää paikkakunnalla {paikkakunta}:")
    print(f"- Kuvaus: {kuvaus}")
    print(f"- Lämpötila: {lämpötila:.1f} Celsius-astetta")
else:
    print("Säätietoja ei voitu hakea.")
