from api.client import Client
from database.models import ModelQuote


def get_data():
    client = Client()
    client.get_data()
        

if __name__ == "__main__":
    get_data()