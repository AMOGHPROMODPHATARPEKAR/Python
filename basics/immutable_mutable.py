

username = "Amogh"
print(username)

# creates a reference in memory
username ="Anil"
print(username)

 
# immutable-who value cannot be changed
# Numbers (int, float, complex)
# Once a number is assigned to a variable, it cannot be changed. For example:
# x = 5
# x = x + 1  # A new object is created with the value 6
# Strings
# Strings are immutable in Python. If you try to modify a string, a new string object will be created instead. For example:
# s = "Hello"
# s = s + " World"  # A new string object is created with the value "Hello World"p
# Tuples
# Tuples are ordered collections of elements and are immutable. Once a tuple is created, you cannot modify its elements. For example:
# t = (1, 2, 3)
# # t[0] = 4  # This will raise a TypeError since tuples are immutable

# mutable: list,dictionaries, array , set


l1=[1,2,3]
l2 = l1;

print(l1)
print(l2)

l1[0] = 2;
print(l1)
print(l2)