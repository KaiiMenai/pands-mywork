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

price = 60
tax = 0.23
txt = f"The price is {price + (price * tax):.2f} euros"
print(txt)