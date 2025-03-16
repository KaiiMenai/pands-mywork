# primes.py
# Generating prime numbers.
# author: Kyra Menai Hamilton

# This was initially done in a naiive way.
# It utilised the code: print (candidate, ' is a prime number.') - this printed all numbers between 2 and 100, but they are not all prime numbers.
# Need to add in an if statement to check that the number is a prime number. 

primes = []                                 # Empty list to store prime numbers.
upto = 101

for candidate in range (2, upto):           # As we want to find prime numbers between 2 and 100, need to make it go up to 101.
    is_prime = True                         # Assume the number is a prime number until proven otherwise.
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            is_prime = False                # If the number is divisible by any number other than 1 and itself then it is not a prime number.
            break                           # If the number is not a prime number, then break out of the loop.

    if is_prime:    
        primes.append(candidate)

print (primes)

# Output 
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]





# Another way to print the answer as a sentence.

# print(f'The prime numbers between 2 and 100 are {primes}.')       # This will print all the prime numbers between 2 and 100.

# Output
    # The prime numbers between 2 and 100 are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].


# To make this more efficient. Make it so that this only checks against primt numbers.

primes = []                                 # Empty list to store prime numbers.
upto = 100001

for candidate in range (2, upto):           
    is_prime = True                         # Only need to check if candidate is divisible by prime.
    for divisor in primes:
        if candidate % divisor == 0:        # If the number is divisible by an int it is not a prime.
            is_prime = False                # Thus no reason to keep checking.
            break                           

    if is_prime:    
        primes.append(candidate)

print (primes)

# END