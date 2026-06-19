# Python Day 1 — List Comprehensions

# Normal way (for loop):
# squares = []
# for n in numbers:
#     squares.append(n * n)

# List comprehension way (one line):
# squares = [n * n for n in numbers]


# Problem 1: Return only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [n for n in numbers if n % 2 == 0]
print(result)  # [2, 4, 6, 8, 10]


# Problem 2: Return words longer than 3 characters
words = ["ai", "data", "ml", "python", "sql", "code"]
result = [word for word in words if len(word) > 3]
print(result)  # ['data', 'python', 'code']


# Problem 3: Return squares of only even numbers
numbers = [1, 2, 3, 4, 5, 6]
square = [n*n for n in numbers if n % 2 == 0]
print(square)  # [4, 16, 36]


# Problem 4: Nested list comprehension (HackerRank - List Comprehensions)
# Given x, y, z, n - print all [i,j,k] where i+j+k != n
x, y, z, n = 1, 1, 2, 3
result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(result)


# Key concepts learned:
# [expression for item in list]                  -> basic
# [expression for item in list if condition]      -> with filter
# [expr for i in range(x) for j in range(y)]       -> nested loops in one line
# Always remember +1 in range() to include the last number
