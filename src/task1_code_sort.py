# TASK 1: AI vs Manual Code Sorting
# Scenario: Sort a list of dictionaries by the 'age' key.

data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# --- 1. Manual Implementation ---
# I wrote this using a standard lambda function
def manual_sort(data):
    return sorted(data, key=lambda x: x['age'])

# --- 2. AI-Suggested Code (Simulated Copilot Suggestion) ---
# Prompt used: "Write a python function to sort list of dicts by age using itemgetter"
from operator import itemgetter
def ai_sort(data):
    return sorted(data, key=itemgetter('age'))

# --- Analysis ---
print("Manual Result:", manual_sort(data))
print("AI Result:", ai_sort(data))

"""
ANALYSIS (For your Report):
The AI suggested using 'operator.itemgetter' instead of a lambda function.
Efficiency: According to Python docs, 'itemgetter' is slightly faster and more memory 
efficient than a lambda function for simple lookups because it is implemented in C. 
The AI version is technically more optimized for large datasets.
"""