# Define the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Define the shift amount
shift = 3

# Get the user input
plaintext = input("Enter a message to encrypt: ")

# Convert the plaintext to lowercase
plaintext = plaintext.lower()

# Initialize the ciphertext
ciphertext = ''

# Loop through each character in the plaintext
for char in plaintext:
    if char in alphabet:
        # Find the position of the character in the alphabet
        position = alphabet.find(char)

        # Shift the position by the specified amount
        new_position = (position + shift) % 26

        # Find the new character from the shifted position
        new_char = alphabet[new_position]

        # Add the new character to the ciphertext
        ciphertext += new_char
    else:
        # If the character is not in the alphabet, add it to the ciphertext as is
        ciphertext += char

# Print the ciphertext
print("The encrypted message is:", ciphertext)
