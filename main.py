from api.client import Client
from database.models import ModelQuote


if __name__ == "__main__":
    client = Client()
    for quote_data in client.get_data():
        model = ModelQuote()
        model.insert_quote(author=quote_data['author'], quote=quote_data['quote'])
