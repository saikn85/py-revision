# 1. Unlimited Precision Signed Integers

int_a = 10 # an integer literal in human readable form - base 10
print(int_a)

# an integer literal in binary form
int_aB = 0b10 
print(int_aB) # results 2

# an integer literal in octet form
int_aO = 0o10
print(int_aO) # results 8

# an integer literal in hexadecimal form
int_aX = 0x10
print(int_aX) # results 16

# Python does not perform implicit conversion, and make it a requirement
# Call the Integer class constructor to get back the value as an integer
conv_int = int('3') # converts string into integer
print(conv_int, type(conv_int))

# produces ValueError - invalid literal for int() with base 10: number
# conv_int2 = int('3.5') 
# print(conv_int2) # Error

# Note when a non-imaginary real number is type casted as int
# rouding of the number is done towards 0!
conv_int3 = int(2.9) # results as 2
print(conv_int3)

conv_int4 = int(2.4) # results as 2
print(conv_int4)

# # Other silly things
# print(--10) # results as 10
# print(-10) # results as -10
# print(-+10) # results as -10

# The 2 optinal argument to the int constructor - base
# int(valid_string_int_literal, base=10); defaults to 10
print(int('10', 2)) # results as 2
print(int('10000', 3)) # results as 81
