# Ask the user for a string input
user_input = input("Enter a sentence or words: ").split()

# Create a list using a for loop (without range function)
word_list = []
for word in user_input:  # Splitting the input into words
    word_list.append(word)  # Adding words to the list

# Print the resulting list
print("List of words:", word_list)

