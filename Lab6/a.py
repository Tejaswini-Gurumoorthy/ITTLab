# Get the user input
string = input("Enter a string: ")

# Convert the string to lowercase and remove all spaces
string = string.lower().replace(" ", "")

# Convert the string to a list
string_list = list(string)

# Reverse the list
reverse_list = string_list[::-1]

# Convert the reverse list back to a string
reverse_string = "".join(reverse_list)

# Check if the original string is equal to the reverse string
if string == reverse_string:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
