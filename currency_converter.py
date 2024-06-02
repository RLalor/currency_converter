import requests

API_KEY = "INSERT YOUR KEY HERE" # They are free from the base url website
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD","CNY", "THB"]
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies{currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print("Sorry we can't convert that currency")
        return None

while True:
    base = input("Enter the base currency (or q for quit): ").upper()
    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue
    del data["CAD"]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
