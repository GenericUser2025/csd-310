import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# Database configuration object
config = {
    'user': 'root',
    'password': '15qtagzb!%QTAGZB',
    'host': 'localhost',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    # Connection Test Code
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    # Verifies that the connection is closed
    if 'db' in locals() and db.is_connected():
        db.close()
        print(" Test connection is closed")
