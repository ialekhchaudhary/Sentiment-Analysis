from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
from urllib.parse import urlparse

# Load environment variables
load_dotenv()

# Get DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set. Please check your configuration.")

# Parse DATABASE_URL for MySQL
parsed_url = urlparse(DATABASE_URL)

db_user = parsed_url.username
db_password = parsed_url.password
db_host = parsed_url.hostname
db_port = parsed_url.port or 3306  # Default MySQL port
db_name = parsed_url.path.lstrip('/')  # Remove leading '/'

# Function to create a MySQL connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
