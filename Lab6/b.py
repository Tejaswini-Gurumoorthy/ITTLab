# Import the string module
import string

# Get the user input
string_with_punctuations = input("Enter a string with punctuations: ")

# Create a list of punctuations
punctuations = list(string.punctuation)

# Convert the string to a list of characters
string_list = list(string_with_punctuations)

# Remove the punctuations from the list of characters
cleaned_list = [char for char in string_list if char not in punctuations]

# Convert the list back to a string
cleaned_string = "".join(cleaned_list)

# Print the cleaned string
print("The string without punctuations is:", cleaned_string)
