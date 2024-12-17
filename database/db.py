import mysql.connector
from dotenv import load_dotenv
import os
from typing import Tuple


load_dotenv()


class DbConnection:
    def __init__(self):
        self.cnx = None
        self.cursor = None

    def __enter__(self) -> Tuple[mysql.connector.cursor.MySQLCursor, mysql.connector.connection.MySQLConnection]:
        try:
            self.cnx = mysql.connector.connect(
                host=os.getenv("HOST"),
                port=os.getenv("PORT"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            self.cursor = self.cnx.cursor()
            return self.cursor, self.cnx
        except Exception as er:
            print("Error connecting:", er)
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def close(self):
        """Close connection
        """
        if self.cursor:
            self.cursor.close()
        if self.cnx:
            self.cnx.close()
