"""Extended Arithmetic Operators"""

# Recall that division always results in a 'float'...
# Unless you use the floor division operator '//' (on the 'int' type)
print("8 // 3 =", 8 // 3)
print("type:", type(8 // 3))
print() # Empty print statements are used as linebreaks here, for readability in the output


# Floor division on 'float' objects still returns a 'float', just rounded to the nearest integer
# Note the difference between the words 'int' (referrring to the type)
# ... and 'integer' (referring to the mathematical definition)
print("33.3 // 8.8 = ", 33.3 // 8.8)
print("type:", type(33.3 // 8.8))
print()


# The modulo operator '%' returns the remainder from division
print("7 % 3 =", 7 % 3) # Because 3 goes into 7 twice with 1 as the remainder
print("6 % 3 =", 6 % 3) # Because 3 goes into 6 twice with 0 as the remainder
print("3 % 12 =", 3 % 12) # This result can be a little unintuitive if you're unfamiliar with modulo
print()


# You can "cast" objects of 'float' to 'int'
print("int(33.3):", int(33.3))
print("type:", type(int(33.3)))
print()


# Beware though: casting rounds DOWN, because it is what's called a 'floor' operation
# If you want to round UP, use round(6.9999)
print("int(6.9999) =", int(6.9999))
print("round(6.9999) =", round(6.9999))
print()


# These two print statements will throw an error, uncomment them and click 'run' to see what kind of error
# print(float('a'))
# print(int('a'))


# Any 'truthy' object casts to the boolean 'True'
print("bool('a'):", bool('a'))


# Any non-'truthy' object casts to the boolean 'False'
print("bool(''):", bool(''))
print("bool(0):", bool(0))
print("bool(0.0)", bool(0.0))


"""
Galvanize Data Science Prep
https://www.galvanize.com/data-science/prep
"""
