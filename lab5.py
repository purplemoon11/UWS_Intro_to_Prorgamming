# Question 1
# Create a fully commented program to:
# Complete this multiplication table:
# X 2 4 6 8 10 12 14 16
# 11
# 7
# 3

# List of column values (multipliers)
# columns = [2, 4, 6, 8, 10, 12, 14, 16]
# List of row values (numbers to be multiplied)
# rows = [11, 7, 3]
# Print the table header
# print("X\t", end="")
# for col in columns:
    # print(col, end="\t")
# print()  # Move to next line
# Loop through each row number
# for row in rows:
    # Print the row label (11, 7, 3)
    # print(row, end="\t")
    # Loop through each column and calculate multiplication
    # for col in columns:
        # print(row * col, end="\t")
    # Move to the next line after each row
    # print()

# Question 2
# In a small highland village, everyone has the surname McIntosh, McGregor, McDonald or McKenzie.
# Everyone is called Angus, Hamish, Morag or Mhairi
# No two people have the same name.
# Create a program to compile a list of the inhabitants of the village.

# List of surnames in the village
# surnames = ["McIntosh", "McGregor", "McDonald", "McKenzie"]
# List of first names in the village
# first_names = ["Angus", "Hamish", "Morag", "Mhairi"]
# List to store all inhabitants
# village = []
# Combine each first name with each surname
# for first in first_names:
#     for last in surnames:
#         full_name = first + " " + last
#         village.append(full_name)
# Print all inhabitants
# print("List of village inhabitants:\n")
# for person in village:
#     print(person)

# Question 3
# (Now try this with a loop – which is best for this problem WHILE or FOR??)
# The code above will randomly set the variable rand_num to be 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9.
# Using that information, create a fully documented program that will randomly choose a number from,
# and including, 1 to 100. Do not display the number.
# Ask the user to guess the number.
# Supply feedback to the user to tell them that their guess was too low or too high and give them another
# guess. When they guess it correctly, tell them how many guesses they took.
import random  # Import random module to generate a random number

# Generate a random number between 1 and 100 (inclusive) syntax random.randrange(start, 101)
# secret_number = random.randrange(1, 101)
# Variable to store user's guess
# guess = None
# Counter to track number of guesses
# guess_count = 0
# Loop until the user guesses correctly
# while guess != secret_number:
    # Ask user for input
    # guess = int(input("Enter your guess (1 to 100): "))
    # Increase guess counter
    # guess_count += 1
    # Check if guess is too low
    # if guess < secret_number:
    #     print("Too low! Try again.")
    # Check if guess is too high
    # elif guess > secret_number:
    #     print("Too high! Try again.")
    # If correct guess
    # else:
    #     print("Correct! You guessed the number.")
    #     print("Total guesses taken:", guess_count)