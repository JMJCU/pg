import sys
from cviceni6 import download_rates

def convert_amount(amount, currency):
    rates = download_rates()

    if currency in rates:
        return amount * rates[currency]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} amount currency")
        sys.exit()

    amount = float(sys.argv[1])
    currency = sys.argv[2]

    print(convert_amount(amount, currency))