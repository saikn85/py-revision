# All integer operations result in an interger, except for the division opertions
a = 10
b = 20

print(f'a + b = {a + b}, type = {type((a + b))}') # results as 30
print(f'a - b = {a - b}, type = {type((a - b))}') # results as -10
print(f'a -- b = {a -- b}, type = {type((a -- b))}') # results as 30
print(f'-a = {-a}, type = {type((-a))}') # results as -10
print(f'a * b = {a * b}, type = {type((a * b))}') # results as 200
print(f'a / b = {a / b}, type = {type((a / b))}') # results as 0.5

# Also called as the Integer Division
# floored quotient of a and b
print(f'a // b = {a // b}, type = {type((a // b))}') # results as 0

# Note: Any operation that involves a float and an int,
# the result of the operation is always a float
print()
print()

a = 5.0

print(f'a + b = {a + b}, type = {type((a + b))}') # results as 25.0
print(f'a - b = {a - b}, type = {type((a - b))}') # results as -15.0
print(f'a -- b = {a -- b}, type = {type((a -- b))}') # results as 25.0
print(f'-a = {-a}, type = {type((-a))}') # results as -5.0
print(f'a * b = {a * b}, type = {type((a * b))}') # results as 10.0
print(f'a / b = {a / b}, type = {type((a / b))}') # results as 0.25

# floored quotient of a and b
print(f'a // b = {a // b}, type = {type((a + b))}') # results as 0