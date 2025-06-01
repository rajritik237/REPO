# Program to take multiple numbers from the user and calculate the average

# Ask the user to input numbers separated by spaces
numbers_input = input("Enter numbers separated by spaces: ")

# Split the input string into a list of strings, then convert to float
numbers = [float(num) for num in numbers_input.split()]

# Calculate the average
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numbers were entered.")
