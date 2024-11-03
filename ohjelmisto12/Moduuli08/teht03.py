import mysql.connector

connection = mysql.connector.connect(
    host="Localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="9642",
    autocommit=True
)


def haeTiedot(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


first_location = haeTiedot(input("Syötä ICAO-koodi\n"))
second_location =hae_tiedot(input("Syötä ICAO-koodi\n"))