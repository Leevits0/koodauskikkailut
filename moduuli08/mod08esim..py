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

cursor = connection.cursor()
cursor.execute("select iso_country, name from country where name = 'APINA'")

# fetchone hakee vain yhden rivin tulosjoukosta
#result_row = cursor.fetchone()
# fetchall() hakee kaikki rivit loput rivit jos esim. fetchone() käytetty ennen sitä.
#print(result_row)

result_rows = cursor.fetchall()
#print(f"Ensimmäinen rivi: {result_rows[0]}, jossa maakoodi: {result_rows[0][0]}")
print(f"Maakoodeja löytyi: {cursor.rowcount} kappaletta")
if cursor.rowcount > 0:
    for row in result_rows:
        print(f"Maakoodi:{row[0]}, Nimi:  {row[1]}")

else:
    print("EI TULOKSIA !!!")

# PAREMPI TAPA
def find_country_by_code(iso_code):
    sql =  f"SELECT name, continent FROM country WHERE iso_country = '{iso_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result


def update_country_name_by_code(iso_code, name):
    sql =  f"UPDATE country set name ='{name}'  WHERE iso_country = '{iso_code}'"
    # tarkasta, että sql on oikein muodostettu
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print(f"Tietue päivitetty {iso_code}: {name}.")
        return True
    print("Päivitys epäonnistui")



code_input = input("Anna maakoodi")
country_input = input("Uusi nimi: ")
update_country_name_by_code(code_input, country_input)



user_input = input("Anna Maakoodi: ")
country = find_country_by_code(code_input)
# Jos country on (erisuuri kuin) --> != None
if country != None:
    print(f" Löydetty maa =  {country[0]}, {country[1]}")
else:
    print("Ei tuloksia.")



