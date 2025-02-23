# money.py
# Prints output using python string formatting 
# author: Kyra Menai Hamilton

# f-strings - (f for format)

  # txt = f"The price is 60 euros"
  # print(txt)

# Modified 08/02/2025 @ 18:30 - added in a placeholder {} - it can contain variables.

  # price = 60
  # txt = f"The price is {price} euros"
  # print(txt)

# Modified 08/02/2025 @ 18:32 - modifier (:) added followed by legal formatting type (i.e. [.2f] - fixed point no. with 2 decimals)

  # price = 60
  # txt = f"The price is {price:.2f} euros"
  # print(txt)

# Modified 08/02/2025 @ 18:37 - value formatted directly.

  # txt = f"The price is {95:.2f} euros"
  #  print(txt)

# Modified 08/02/2025 @ 18:39 - math operation in the placeholder.

  # txt = f"The price is {20 * 60} euros"
  # print(txt)

# Modified 08/02/2025 @ 18:41 - performing math operation on vatiables.

  # price = 60
  # tax = 0.23
  # txt = f"The price is {price + (price * tax)} euros"
  # print(txt)

# Modified 08/02/2025 @ 18:43 - :.2f added back to give 2dp.

  # price = 60
  # tax = 0.23
  # txt = f"The price is {price + (price * tax):.2f} euros"
  # print(txt)

# Modified 08/02/2025 @ 18:45 - if...else statement for responses > Return "Expensive" if the price is over 70, otherwise return "Cheap"

  # price = 90
  # tax = 0.23
  # txt = f"It is very {'Expensive' if price>70 else 'Cheap'}"
  # print(txt)

  # price = 50
  # tax = 0.23
  # txt = f"It is very {'Expensive' if price>70 else 'Cheap'}"
  # print(txt)

# Modified 08/02/2025 @ 18:49 - Executing functions in f-strings 
# Using fruit as an example - use upper() to convert value to upper case letters.

  # fruit = "raspberries"
  # txt = f"I love {fruit.upper()}"
  # print(txt)

# Modified 08/02/2025 @ 18:54 - not required to use built-in python methods, can create own functions (i.e. converting feet into meters)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude."
print(txt)

# END