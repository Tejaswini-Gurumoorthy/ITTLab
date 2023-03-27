# Get the user input for the sentence
sentence = input("Enter a sentence: ")

# Convert the sentence to a list of words
words = sentence.split()

# Sort the words in alphabetical order
sorted_words = sorted(words)

# Convert the sorted words list back to a string
sorted_sentence = " ".join(sorted_words)

# Print the sorted sentence
print("The sorted sentence is:", sorted_sentence)
