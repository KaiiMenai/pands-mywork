# messingwithdictionary2.py
# Exploring the use of dictionaries in Python.
# author: Kyra Menai Hamilton

# Making a car database using a dictionary.

car = {                             
    'make': 'Volvo',                
    'model': 'XC70',                
    'year': 2007,                   
    'owner' : {                     
        'name' : 'Mungo',
        'driver number' : 1856,
        },                     
    'tags': ['Estate', 'Used']        
}

# print(car)                          # This is basic.
    # Output
        # {'make': 'Volvo', 'model': 'XC70', 'year': 2007, 'owner': {'name': 'Mungo', 'driver number': 1856}, 'tags': ['Estate', 'Used']}

# print(car['owner']['name'])       # To access a specific key in the dictionary, use square brackets and the key name.# for key in car:

# This is an improvement:
# print (key)                     # This will print out all the keys in the dictionary.
    # Output
        # make
        # model
        # year
        # owner
        # tags

# This gives even more specific details from the dictionary:
# for key in car:
    # print (key, ' has value ', car[key])
        # Output
            # make  has value  Volvo
            # model  has value  XC70
            # year  has value  2007
            # owner  has value  {'name': 'Mungo', 'driver number': 1856}
            # tags  has value  ['Estate', 'Used']


# A better version would be:

for key, value in car.items():
    print (key, 'has value', value)         # The comma will automatically put a space in, so no need to add in an extra (as seen above - it looks messy) 

# Output
    # make has value Volvo
    # model has value XC70
    # year has value 2007
    # owner has value {'name': 'Mungo', 'driver number': 1856}
    # tags has value ['Estate', 'Used']

# END