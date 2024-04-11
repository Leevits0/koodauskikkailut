import mysql.connector

connection = mysql.connector.connect(
    host="Localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="9642",
    autocommit=True
)
print(connection)

def lentoasema(ICAO):
    sql = f"SELECT name FROM airport WHERE ident = '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result

