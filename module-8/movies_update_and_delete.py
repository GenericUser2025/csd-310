# Paul Singleton > CSD310: Module 8.2 > 7/7/2024
import mysql.connector

# This is the function used to display the films
def show_films(cursor, title):
    cursor.execute("""
        SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    
    films = cursor.fetchall()
    
    print(f"\n-- {title} --\n")
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre: {film[2]}")
        print(f"Studio Name: {film[3]}\n")

# Connects to MySql database using my credentials
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="15qtagzb!%QTAGZB",
    database="movies"
)
cursor = db.cursor()

# Shows the films before any edits or changes are made
show_films(cursor, "DISPLAYING FILMS")

# Since I didn't want to use a previous studio, I needed to check to see if Warner Bros existed
cursor.execute("SELECT studio_id FROM studio WHERE studio_name = 'Warner Bros.'")
studio_id = cursor.fetchone()

if not studio_id:
    print("Inserting studio 'Warner Bros.' into the studio table.")
    insert_studio_query = "INSERT INTO studio (studio_name) VALUES ('Warner Bros.')"
    try:
        cursor.execute(insert_studio_query)
        db.commit()
        # Fetches for the Warner Studio once more
        cursor.execute("SELECT studio_id FROM studio WHERE studio_name = 'Warner Bros.'")
        studio_id = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
        db.close()
        exit()

# Inserts a new film with the release date of the movie
insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES ('Interstellar', '2014', 169, 'Christopher Nolan', %s, 2)
"""
try:
    cursor.execute(insert_query, (studio_id[0],))
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    db.rollback()

# Updates the Alien movie - genre to > Horror
update_query = """
    UPDATE film 
    SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') 
    WHERE film_name = 'Alien'
"""
try:
    cursor.execute(update_query)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    db.rollback()

# Deletes the film labeled as 'Gladiator'
delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
try:
    cursor.execute(delete_query)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETION")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    db.rollback()

db.close()