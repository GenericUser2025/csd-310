# Paul Singleton - CSD310_Module 7.2 - 7/7/2024
import mysql.connector
from mysql.connector import Error

try:
    # Connects to MySql Database using my admin credentials
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="15qtagzb!%QTAGZB",
        database="movies"
    )

    cursor = db.cursor()

    # Selects everything from the studio table within the movies database
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("--DISPLAYING studio RECORDS--")
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}\n")

    # Selects everything from the genre table within the movies database
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("--DISPLAYING genre RECORDS--")
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}\n")

    # Selects the runtime from the film table within the movies database
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_movies = cursor.fetchall()
    print("--DISPLAYING Short Film RECORDS--")
    for movie in short_movies:
        print(f"Film Name: {movie[0]}")
        print(f"Runtime: {movie[1]}\n")

    # Selects the film name from the film table within the movies database
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    movies_by_director = cursor.fetchall()
    print("--DISPLAYING Director RECORDS in Order--")
    for movie in movies_by_director:
        print(f"Film Name: {movie[0]}")
        print(f"Director: {movie[1]}\n")

except Error as e:
    print(f"Error: {e}")
finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("The SQL connection is officially closed")