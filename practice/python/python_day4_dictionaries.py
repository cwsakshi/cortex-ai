# Python Day 4 — Dictionaries Deep Dive

# Useful dictionary methods:
# d.keys()    -> all keys
# d.values()  -> all values
# d.items()   -> key-value pairs together


# Problem 1: Count how many times each word appears (if/else version)
words = ["ai", "ml", "ai", "data", "ml", "ai"]

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(words))  # {'ai': 3, 'ml': 2, 'data': 1}


# Problem 2: Same thing using .get() shortcut
def count_words_get(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

print(count_words_get(words))  # {'ai': 3, 'ml': 2, 'data': 1}


# Problem 3: Loop through dictionary using .items()
counts = {'ai': 3, 'ml': 2, 'data': 1}

for word, count in counts.items():
    print(f"{word} appears {count} times")

# Output:
# ai appears 3 times
# ml appears 2 times
# data appears 1 times


# Key concepts learned:
# counts[word] = counts.get(word, 0) + 1  -> clean way to count occurrences
# for key, value in d.items():            -> unpacks key-value pairs while looping
# d.keys() / d.values() / d.items()       -> access different parts of a dict
# This counting pattern is heavily tested in interviews (word frequency, anagrams, etc.)
