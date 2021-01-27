# Practice: In this practice problem the objective is to print the names of the borders for each of the countries.

# Step 1:
import requests

# Step 2:
url = 'https://restcountries.eu/rest/v2/all'

# Step 3:
response = requests.get(url)

# Step 4:
storage = response.json()

# Solution:

for item in range(len(storage)):
     border = storage[item]['borders']
     for item in border:
          print(item)

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
print(storage[0]['borders'])

# Step 10:
print(type(storage[0]['borders']))

# Step 11:
print(storage[0]['borders'][0])

# Step 12:
 for item in range(len(storage)):
     border = storage[item]['borders']
     for item in border:
          print(item)
