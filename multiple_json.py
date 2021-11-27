# Step 1:
import requests

# Step 2:
url = 'https://restcountries.eu/rest/v2/all'

# Step 3:
response = requests.get(url)

# Step 4:
storage = response.json()

# Solution:

storage[0]['currencies'][0]['code']

# Workflow

# Step 5: 
print(type(storage))

# Step 6:
print(len(storage))

# Step 7:
print(storage[0])

# Step 8:
print(type(storage[0]))

# Step 9:
print(storage[0]['currencies'])

# Step 10:
print(type(storage[0]['currencies']))

# Step 11:
print(storage[0]['currencies'][0])

# Step 12:
print(type(storage[0]['currencies'][0]))

# Step 13:
print(storage[0]['currencies'][0]['code'])

# Step 14:
 for item in range(len(storage)):
     print(storage[item]['currencies'][0]['code'])
