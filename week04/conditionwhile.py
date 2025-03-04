# conditionwhile.py
# author: Kyra Menai Hamilton

# Running Tasks Based on a Condition With while Loops

# A general use case for a while loop is waiting for a resource to become available before proceeding to use it. 
# This is common in scenarios like the following:
    # Waiting for a file to be created or populated.
    # Checking whether a server is online.
    # Polling a database until a record is ready.
    # Ensuring a REST API is responsive before making requests.

# Here’s a loop that continually checks if a given file has been created:

import time
from pathlib import Path

# filename = Path("hello.txt")

# print(f"Waiting for {filename.name} to be created...")

# while not filename.exists():
#     print("File not found. Retrying in 1 second...")
#     time.sleep(1)

# print(f"{filename} found! Proceeding with processing.")
# with open(filename, mode="r") as file:
#     print("File contents:")
#     print(file.read())

# This code will contine to loop if run as there is no hello.txt file.

# Using while Loops for an Unknown Number of Iterations

# while loops are also great when you need to process a stream of data with an unknown number of items. 
# In this scenario, you don’t know the required number of iterations, so you can use a while loop with True as its control condition. 
# This technique provides a Pythonic way to write loops that will run an unknown number of iterations.

# Example: 

# Suppose you need to read a temperature sensor that continuously provides data. 
# When the temp is equal to or greater than 28 degrees C, you should stop monitoring it. 
# Here’s a loop to accomplish this task:

import random
import time

def read_temperature():
    return random.uniform(20.0, 30.0)

while True:
    temperature = read_temperature()
    print(f"Temperature: {temperature:.2f}°C")

    if temperature >= 28:
        print("Required temperature reached! Stopping monitoring.")
        break

    time.sleep(1)

# References:
# https://realpython.com/python-while-loop/

# END