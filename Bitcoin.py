#import requests
import requests
import colorma
#url api
ticket_api = 'https://ai.coinmarketcap.com/va/ticker/'
#function to get the specific crypto from the url in gbp
def latest_crypto(crypto):
    response = requests.get(ticker_api + crypto)
    response_json = response.json()
    return float(response_json[0]['price_gbp'])
# call function
latest_crypto(bitcoin)
#main program that specifies the crypto type, calls the latest price and prints
def main():
    prev_price = -1
    while True:
        crypto = 'bitcoin'
        price = latest_crypto(crypto)

        if price != prev_price:
            print('Bitcoin Price' , price)
            if price >= (1.1* prev_price):
                print(Fore.GREEN , price)
            elif price <= (0.9*prev_price):
                print(Fore.RED, price)
            prev_price = price
main()


