# messingwithdictionary.py
# Exploring the use of dictionaries in Python.
# author: Kyra Menai Hamilton

# Making a car database using a dictionary.

car = {                             # Dictionary with key-value pairs.
    'make': 'Ford',                 # For dictionary objects : pairs up the keys and values.
    'model': 'Focus',               # The key is the name of the value. The value is the data
    'year': 2000,                   # All keys are unique and are strings.
    'owner' : {                     # Values can be any data type.
        'name' : 'Rohan',
        'driver number' : 1123,
        },                     
    'tags': ['sedan', 'new']        # This is a list within the dictionary.
}

print(car)                          # This will print out the dictionary.

# Output
    # {'make': 'Ford', 'model': 'Focus', 'year': 2000, 'owner': 'Rohan', 'tags': ['sedan', 'new']}

# print(car['owner']['name'])       # To access a specific key in the dictionary, use square brackets and the key name.

# Can define things as attributes of a class. i.e. car.make, car.model, car.year, car.owner, car.tags and to define it would be something like attr = X.
# Dictionary objects can get quite complicated depending on the amount/type of data being stored.

# END