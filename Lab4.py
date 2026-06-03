#Iteration - Syntax for variable in sequence range(start, stop, step)

# Question 1
# Create a fully commented program to:
# count down and display from 10 to 1 and then display “Blast Off”

#Start the countdown from 10 where we want to print it to 0 as stop value is often excluded and then the step -1
# for i in range(10, 0, -1):
#     print(i)
#print blast off
# print("Blast off")

#Question 2
# Program to display the first 13 odd numbers
# and calculate their total sum

# Variable to store the sum of odd numbers
# total = 0
# Variable to count how many odd numbers have been displayed
# count = 0
# Start checking numbers from 0
# number = 0
# Repeat until 13 odd numbers are displayed
# while count < 13:
    # Check if the number is odd
    # if number % 2 != 0:
        # Display the odd number
        # print(number)
        # Add the odd number to the total
        # total = total + number
        # Increase the count of odd numbers displayed
        # count = count + 1
    # Move to the next number
    # number = number + 1
# Display the final sum
# print("Sum =", total)

# Question 3
# Edit Q2 to allow the user to choose
# a) how many odd numbers they want to sum (starting from 0)
# b) how many odd numbers they want to sum (starting from a number of their choice)

# n = int(input("Enter a number you want to sum: "))
# total = 0
# count = 0
# number = 0
#
# while count < n:
#     if number % 2 != 0:
#         print(number)
#         total = total + number
#         count = count + 1
#     number = number + 1
# print("Sum =", total)

# n = int(input("Enter a number you want to sum: "))
# start = int(input("Enter the starting number: "))
# total = 0
# count = 0
# number = 0
#
# while count < n:
#     if number % 2 != 0:
#         print(number)
#         total = total + number
#         count = count + 1
#
#     number = number + 1
#
# print("Sum =", total)

# Question 4
# There are six characters in the game Cluedo (Miss Scarlett, Professor Plum, Mrs Peacock, Reverend
# Green, Colonel Mustard and Dr Orchid).
# Create a list with these names in it.
# Use a FOR loop to go through the list, displaying for each name in turn the prompt “Do you find the
# accused, <character name>, guilty or not guilty?”. The user should enter “Guilty” or “Not Guilty”.
# Create a fully commented program to do this.
# Create a list of Cluedo characters

# characters_name = [
#     "Miss Scarlett",
#     "Professor Plum",
#     "Mrs Peacock",
#     "Reverend Green",
#     "Colonel Mustard",
#     "Dr Orchid"
# ]
# # Loop through each character in the list
# for name in characters_name:
#     # Ask the user for input for each character
#     answer = input(f"Do you find the accused, {name}, guilty or not guilty? ")
#     # Display what the user entered
#     print(f"You marked {name} as: {answer}")
# print("All characters have been evaluated.")
