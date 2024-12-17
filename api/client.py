import requests


class Client:
    def __init__(self, url: str = "http://api.forismatic.com/api/1.0/") -> None:
        """
        Class for work with API Forismatic
        Args:
            url (str): URL API. Defaults to "http://api.forismatic.com/api/1.0/".
        """
        self.url = url

    def get_data(self) -> dict[str, str]:
        """
        Get data from API
        Returns:
            dict: Data form API (format=dict) (data=author, quote)
        """
        params: dict[str, str | int] = {
            "method": "getQuote",
            "format": "json",
            "key": 457653,
            "lang": "en"
        }

        try:
            for _ in range(11):
                with requests.Session() as session:
                    response = session.get(self.url, params=params)
                    response.raise_for_status()  
                    response = response.json()
                    print( {"author": response["quoteAuthor"], "quote": response["quoteText"]}  )
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {}
