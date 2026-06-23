# Python Day 5 — List Slicing

nums = [10, 20, 30, 40, 50]

print(nums[1:3])    # [20, 30]  -> elements from index 1 up to (not including) 3
print(nums[:2])      # [10, 20] -> from start up to index 2
print(nums[-2:])     # [40, 50] -> last 2 elements
print(nums[::-1])    # [50, 40, 30, 20, 10] -> entire list reversed


# Why [::-1] reverses a list:
# The third value in slicing is the STEP.
# -1 as step means "move backward one position at a time, starting from the end"
# This is a common trick for reversing strings/lists without a loop

s = "hello"
print(s[::-1])   # "olleh"


# Key concepts learned:
# nums[start:end]     -> slice from start up to (not including) end
# nums[:end]          -> from beginning up to end
# nums[start:]        -> from start to the end of list
# nums[-n:]           -> last n elements
# nums[::-1]          -> reverses the entire list/string
# Used in: Rotate Array, Palindrome checks, reversing data
