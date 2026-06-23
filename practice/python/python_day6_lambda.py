# Python Day 6 — Lambda Functions

# A lambda is a small, one-line anonymous function
square = lambda x: x * x
print(square(5))  # 25

# Same as writing:
# def square(x):
#     return x * x


# Most common real use — sorting with a custom key
students = [("Sakshi", 85), ("Rahul", 70), ("Priya", 92)]

# Sort by score (second item in each tuple), highest first
result = sorted(students, key=lambda x: x[1], reverse=True)
print(result)
# [('Priya', 92), ('Sakshi', 85), ('Rahul', 70)]


# Key concepts learned:
# lambda arguments: expression   -> shorthand for a quick one-line function
# key=lambda x: x[1]             -> tells sorted() what to sort by
# x[0] = first item in tuple, x[1] = second item, same indexing as lists/arrays
# reverse=True                   -> sorts descending (highest first)
# This pattern is used everywhere: sorting dicts by value, objects by attribute, custom comparisons
