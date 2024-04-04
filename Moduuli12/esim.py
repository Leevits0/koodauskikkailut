# Moduuli 12 esimerkit
 # try / except virheenkorjaus:
import requests


def search_shows(search_term):
    url = (f"https://api.tvmaze.com/search/shows?q={search_term}")
    try:
        response = requests.get(url)
        print(f"HTTP response status scode: {response.status_code}")
        shows = response.json()
        #print(f"Ensimmäisen sarjan nimi: {shows[0]['show']['name']}")
        #Tulostetaan kaikki hakutulokset
        if response.status_code == 200:
            print(f"Ohjelmahaun tulokset hakusanalla: {search_term}")
            for show in shows:
                # Haetaan genret sisäkkäisellä silmukalla/loopilla
                genres = ""
                for genre in show['show']['genres']:
                    genres = genres + genre
                print(f"{show['show']['name']}  ( {genres}: )  {show['show']['url']}")
                
    except requests.exceptions.RequestException as error:
        print("HTTP-pyyntö epäönnistui. Ei verkkoyhteyttä palvelimeen")
        print(error)
    except Exception as error:
        print("HTTP-pyyntö epäonnistui")
        print(error)
    except ValueError:
        print("Jotain meni pieleen....")

search_input = input("Anna hakusana:")
search_shows(search_input)


