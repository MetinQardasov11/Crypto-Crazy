import requests


def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONdataset/master/crypto.json")

    if response.status_code == 200:
        return response.json()
        

crypto_response = get_crypto_data()
user_input = input("Enter a cryptocurrency name: ")

for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(f"Currency: {crypto['currency']}")
        print(f"Price: {crypto['price']}")