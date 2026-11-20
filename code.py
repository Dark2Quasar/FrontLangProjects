# Importing the sys module to get the version of python
import sys

print("Python version:", sys.version)

# List of built-in keywords
builtins = dir(__builtins__)

# Printing the list of built-in keywords
print("Built-in Keywords:")
for keyword in builtins:
    print(keyword)