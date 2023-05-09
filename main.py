import json
import requests

# Set the URL template
url_template = "https://unisat.io/brc20-api-v2/brc20/{ticker}/holders?start=0&limit={numberOfHolders}"

# Replace {ticker} and {numberOfHolders} with the actual values you can see the holders on unisat.io
ticker = "subC"
number_of_holders = 336

# Format the URL with the actual values
url = url_template.format(ticker=ticker, numberOfHolders=number_of_holders)

# Fetch the JSON data from the URL
response = requests.get(url)
json_data = response.json()

# Extract the addresses
addresses = [detail['address'] for detail in json_data['data']['detail']]

# Save the addresses to a new file named 'addresses.txt'
with open('addresses.txt', 'w') as addresses_file:
    for address in addresses:
        addresses_file.write(address + '\n')