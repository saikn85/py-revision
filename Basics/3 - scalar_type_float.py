# 2. Floating Points => Adopts IEEE - 754 double precision with 53-bits
# of binary precision with approx. 15 - 16 significant digits in the decimal

float_a = 3.123 # float literal
print(float_a)

# float's scientific notation, e is base 10
float_aB = 3e8 # results as 300000000.0
print(float_aB)

PLANKS = 1.616e-35 # Plank's Constant
print(PLANKS)

# Call the float(number) constructor to perform the required conversion
print(float(3), float('3')) # results as 3.0

PLANKS_STRING = '1.616e-35' # Plank's Constant string representation
conv_planks = float(PLANKS_STRING)
print(conv_planks, type(conv_planks))

# Special Numbers in float
print(float('nan')) # Not-a-Number
print(float('inf')) # +ve infinity
print(float('-inf')) # -ve infinity