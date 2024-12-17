from .db import DbConnection

class ModelQuote:
    def __init__(self) -> None:
        """Get connect with db"""
        with DbConnection() as (cursor, cnx):
            self.cursor = cursor
            self.cnx = cnx
            
    def create_table(self) -> None:
        """
        Create table quote
        """
        query = """
            CREATE TABLE IF NOT EXISTS `quote` (
                quote_id INT PRIMARY KEY AUTO_INCREMENT,
                author VARCHAR(100) NOT NULL,
                quote TEXT NOT NULL
            )
        """
        try:
            self.cursor.execute(query)
            self.cnx.commit()
        except Exception as err:
            print("Error execute", err)
            
    def insert_quote(self, author: str, quote: str) -> None:
        query = f"""
            INSERT INTO `quote` (author, quote)
            VALUES (%s, %s)
        """
        try:
            self.cursor.execute(query, (author, quote))
            self.cnx.commit()
            print(f"[+] Author: {author} inserted...")
        except Exception as err:
            print("Error execute", err)

