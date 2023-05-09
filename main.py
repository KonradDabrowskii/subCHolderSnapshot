import json

# Read the JSON data from the 'holders.json' file
with open('holders.json', 'r') as json_file:
    json_data = json.load(json_file)

# Extract the addresses
addresses = [detail['address'] for detail in json_data['data']['detail']]

# Save the addresses to a new file named 'addresses.txt'
with open('addresses.txt', 'w') as addresses_file:
    for address in addresses:
        addresses_file.write(address + '\n')