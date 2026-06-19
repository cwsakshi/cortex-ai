# Python Day 2 — Functions

# A function is a reusable block of code
# def function_name(parameters):
#     return value

# Problem 1: Check if a number is even
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False


# Problem 2: Sum of only even numbers in a list
def sum_of_evens(nums):
    return sum([n for n in nums if n % 2 == 0])

print(sum_of_evens([1, 2, 3, 4, 5, 6]))  # 12


# Problem 3: Check if a string is a palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False


# Key concepts learned:
# - def keyword defines a function
# - return sends back a value and exits the function
# - functions can combine with list comprehension: sum([n for n in nums if ...])
# - functions can reuse logic from previous problems (two pointers)
