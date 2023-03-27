import re

# Define the input string
input_str = "The quick brown fox jumped over the lazy dog."

# Define the pattern to find
pattern = r"brown"

# Define the replacement string
replacement_str = "red"

# Use the sub() function to find and replace the pattern in the input string
output_str = re.sub(pattern, replacement_str, input_str)

# Print the original and updated strings
print("Original string:", input_str)
print("Updated string:", output_str)
