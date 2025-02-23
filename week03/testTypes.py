# testTypes.py
# This program will involve exploring variable types and the functions around them.
# author: Kyra Menai Hamilton

# Lab 3.1
# Five types of variables are below. The print function following the initial variable list is used to discern the type that each variable belongs to.

i = 3                      # int
fl = 3.5                   # float
isa = True                 # boolean(bool)
memo = 'how now Brown Cow' # str
lots = []                  # list

print('variable {} is of type:{} and value:{}'.format('i', type(i), i))
print('variable {} is of type:{} and value:{}'.format('fl', type(fl), fl))
print('variable {} is of type:{} and value:{}'.format('is', type(isa), isa))
print('variable {} is of type:{} and value:{}'.format('memo', type(memo), memo))
print('variable {} is of type:{} and value:{}'.format('lots', type(lots), lots))

# Output:
    # variable i is of type:<class 'int'> and value:3
    # variable fl is of type:<class 'float'> and value:3.5
    # variable is is of type:<class 'bool'> and value:True
    # variable memo is of type:<class 'str'> and value:how now Brown Cow
    # variable lots is of type:<class 'list'> and value:[]

# END