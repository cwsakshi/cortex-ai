# Python Day 7 — Try/Except Error Handling

# try/except catches errors gracefully instead of crashing the program

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except Exception as e:
        print(f"Error: {e}")
        return "Cannot divide by zero"


print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # "Cannot divide by zero"


# Key concepts learned:
# try block        -> attempt risky code (division, API calls, file access, etc.)
# except Exception as e  -> catches ANY error type, stores details in variable e
# Must return inside BOTH try and except blocks
#   - forgetting return in except = function silently returns None
#   - same bug pattern as forgetting "return -1" in Binary Search
#
# Real-world use: this exact pattern was used in Cortex AI's career_agent.py
# to handle Tavily API failures and LLM call failures gracefully, so the
# app shows a friendly message instead of crashing when something goes wrong.
