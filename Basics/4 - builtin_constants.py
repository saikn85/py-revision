# 3. Constants that live in the built-in namespace
# The below are most commonly used

# 3.1 True - The true value of the bool type. 
# Assignments to True are illegal and raise a SyntaxError.
# That is True = anything # Is not allowed!

# 3.2 False - The false value of the bool type. 
# Assignments to False are illegal and raise a SyntaxError.
# That is False = anything # Is not allowed!

# An object can be converted into a boolean value by calling the
# bool constructor
print(bool(3)) # returns True
print(bool(0), bool(0.0), bool(complex(0, 0)), bool(None)) # returns False
print(bool(""), bool([]), bool(())) # returns False

# 3.3 None - An object frequently used to represent the absence of a value,
# as when default arguments are not passed to a function.
# Assignments to None are illegal and raise a SyntaxError.
# None is the sole instance of the NoneType type.
# That is None = anything # Is not allowed!
variable_a = None # Does nothing, Na da!!!

# Note: on a Python REPL session, the _ (underscore) stores the result of
# the previously executed statement/ expression

# Note:
# By default, an object is considered true unless its class defines either
# a __bool__() method that returns False or a __len__() method that returns zero,
# when called with the object.