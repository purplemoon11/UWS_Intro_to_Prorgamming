# Question 1
# Create a fully commented version of the A/S/M/D from the lecture.

# Display the menu options
# print("MENU")
# print("A - Add")
# print("S - Subtract")
# print("M - Multiply")
# print("D - Divide")
# Get user's choice
# choice = input("Enter your choice: ").upper()
# Ask the user for two numbers
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# Check which operation the user selected
# if choice == "A":
#     answer = num1 + num2
#     print("Answer =", answer)
# elif choice == "S":
#     answer = num1 - num2
#     print("Answer =", answer)
# elif choice == "M":
#     answer = num1 * num2
#     print("Answer =", answer)
# elif choice == "D":
    # Prevent division by zero
#     if num2 == 0:
#         print("Cannot divide by zero")
#     else:
#         answer = num1 / num2
#         print("Answer =", answer)
# else:
    # Handles invalid menu choices
    # print("Invalid choice")

# Question 2
# Add Modulus, Floor Division and Exponentiation to your program from Q1

# print("MENU")
# print("A - Add")
# print("S - Subtract")
# print("M - Multiply")
# print("D - Divide")
# print("% - Modulus")
# print("// - Floor Division")
# print("** - Exponent")
# Take menu input
# choice = input("Choose operation: ")
# Take numbers
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# if choice == "A":
#     print(num1 + num2)
# elif choice == "S":
#     print(num1 - num2)
# elif choice == "M":
#     print(num1 * num2)
# elif choice == "D":
#     if num2 == 0:
#         print("Cannot divide by zero")
#     else:
#         print(num1 / num2)
# elif choice == "%":
#     print(num1 % num2)
# elif choice == "//":
#     print(num1 // num2)
# elif choice == "**":
#     print(num1 ** num2)
# else:
#     print("Invalid option")

# Question 3
# Create a fully commented program to:
# allow a user to view one of the principles of python (Zen of Python).

# Store Zen principles in a dictionary
# zen = {
# 1: "Beautiful is better than ugly.",
# 2: "Explicit is better than implicit.",
# 3: "Simple is better than complex.",
# 4: "Complex is better than complicated.",
# 5: "Readability counts."
# }
# Display menu
# print("Zen of Python Principles")
# for number, saying in zen.items():
#     print(number, "-", saying)
# Ask user to choose
# choice = int(input("\nChoose a principle number: "))
# Display selected principle
# if choice in zen:
#     print("\nYour selected principle:")
#     print(zen[choice])
# else:
#     print("Invalid choice")

# Question 4
# Create a fully commented program to:
# allow a user to select a member of the Monty Python team and view details of their date of
# birth, place of birth and middle name(s) in any.

# Store member details
# members = {
# "1": {
# "name": "John Cleese",
# "dob": "27 October 1939",
# "birth": "Weston-super-Mare, England",
# "middle": "Marwood"
# },
# "2": {
# "name": "Eric Idle",
# "dob": "29 March 1943",
# "birth": "South Shields, England",
# "middle": "None"
# },
# "3": {
# "name": "Michael Palin",
# "dob": "5 May 1943",
# "birth": "Sheffield, England",
# "middle": "Edward"
# },
# "4": {
# "name": "Graham Chapman",
# "dob": "8 January 1941",
# "birth": "Leicester, England",
# "middle": "Arthur"
# }
# }
# Show menu
# print("Monty Python Members")
# for key, person in members.items():
#     print(key, "-", person["name"])
# User selection
# choice = input("\nSelect member: ")
# Display information
# if choice in members:
#     person = members[choice]
#     print("\nName:", person["name"])
#     print("Date of Birth:", person["dob"])
#     print("Place of Birth:", person["birth"])
#     print("Middle Name(s):", person["middle"])
# else:
#     print("Invalid selection")