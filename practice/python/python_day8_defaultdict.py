# Python Day 8 — defaultdict

from collections import defaultdict

# defaultdict(list) means: if a key doesn't exist yet, automatically
# create it with an empty list [] BEFORE doing anything else.
# This removes the need for manual "if key in dict else" checks.


# OLD WAY (manual if/else) - from Group Anagrams Day 15
words = ["eat","tea","tan","ate","nat","bat"]
groups_old = {}

for word in words:
    key = "".join(sorted(word))
    if key in groups_old:
        groups_old[key].append(word)
    else:
        groups_old[key] = [word]

print(list(groups_old.values()))


# NEW WAY using defaultdict - same loop structure, simpler inner logic
groups_new = defaultdict(list)

for word in words:
    key = "".join(sorted(word))
    groups_new[key].append(word)   # no if/else needed - auto-creates [] if key is new

print(list(groups_new.values()))

# Both produce the SAME output:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# Key concepts learned:
# defaultdict(list) - auto-creates an empty list for any new key
# defaultdict(int)  - auto-creates 0 for any new key (useful for counting)
# defaultdict(set)  - auto-creates an empty set for any new key
# The LOOP structure stays the same - only the "does key exist" check disappears
# Cleaner code for the exact same grouping/counting pattern used throughout DSA practice
