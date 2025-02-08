# nmoney.py
# Prints output using python string formatting 
# author: Kyra Menai Hamilton

# f-strings - (f for format)

# Modified 08/02/2025 @ 18:30 - added in a placeholder {} - it can contain variables.
# Modified 08/02/2025 @ 18:32 - modifier (:) added followed by legal formatting type (i.e. [.2f] - fixed point no. with 2 decimals)
# Modified 08/02/2025 @ 18:37 - value formatted directly.
# Modified 08/02/2025 @ 18:39 - math operation in the placeholder.
# Modified 08/02/2025 @ 18:41 - performing math operation on vatiables.
# Modified 08/02/2025 @ 18:43 - :.2f added back to give 2dp.
# Modified 08/02/2025 @ 18:45 - if...else statement for responses > Return "Expensive" if the price is over 70, otherwise return "Cheap"

# price = 50
# tax = 0.23
# txt = f"It is very {'Expensive' if price>70 else 'Cheap'}"
# print(txt)

# Modified 08/02/2025 @ 18:49 - Executing functions in f-strings 
# using fruit as an example - use upper() to convert value to upper case letters.

fruit = "raspberries"
txt = f"I love {fruit.upper()}"
print(txt)