import mysql.connector 
from mysql.connector import Error

def create_database(host, user, passwd, database_name):
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host=host,         # Typically 'localhost' for local databases
            user=user,         # 'root' is the common admin user
            password=passwd    # Password for the MySQL user
        )

        # Check if the connection is successful
        if connection.is_connected():
            print('Connected to MySQL server')

        # Create a new database
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully!")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Specify your MySQL server details
host = "localhost"
user = "root"
passwd = "root"
database_name = "TwitterDB"

# Create the database
create_database(host, user, passwd, database_name)
