import requests
import random
from typing import Dict, Generator

class Client:
    def __init__(self, url: str = "http://api.forismatic.com/api/1.0/") -> None:
        """
        Class for working with the Forismatic API.
        Args:
            url (str): The API URL. Defaults to "http://api.forismatic.com/api/1.0/".
        """
        self.url = url

    def get_data(self) -> Generator[Dict[str, str], None, None]:
        """
        Fetches data from the API and yields quotes and their authors.
        Returns:
            Generator: A generator yielding dictionaries with keys 'author' and 'quote'.
        """
        try:
            for _ in range(11):
                params = {
                    "method": "getQuote",
                    "format": "json",
                    "key": random.randint(1, 999),  
                    "lang": "en"
                }
                with requests.Session() as session:
                    response = session.get(self.url, params=params)
                    response.raise_for_status()  
                    response_json = response.json()  

                    yield {"author": response_json["quoteAuthor"], "quote": response_json["quoteText"]}

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {}
