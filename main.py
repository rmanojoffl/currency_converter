""
using exchaangerate api for real time exchange data 

"""

import requests

base_currency=input("Enter the currency you are converting from :").upper()
converting_currency=input("Enter the symbol of the currency you want to convert : ").upper()
amount_of_currency=int(input("Enter the amount of currency you want to convert to : "))



#api parameters
api_key="76589739e0a3bbdd44beb729"

response=requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}")
response.raise_for_status

try:
    converting_currency_rate=response.json()["conversion_rates"][converting_currency]
    

    converted_amount=amount_of_currency*converting_currency_rate

    print(f"{converted_amount} {converting_currency}")
except KeyError:
    print("The provided currrency pair is wrong or not found in the exchange data")
