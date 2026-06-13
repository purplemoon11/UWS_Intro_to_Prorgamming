# import math

# Question 1
# Create a fully commented program to:
# Ask a user for a number of degrees between 0 and 360.
# The program should output the value of the sine, cosine and tangent of the angle.
# (Hint: you might need to convert degrees to radians first!!)

# def degree(deg):
#     radian = math.radians(deg)
#     sin = math.sin(radian)
#     cos = math.cos(radian)
#     tan = math.tan(radian)
#     print(f"sin: {sin}")
#     print(f"cos: {cos}")
#     print(f"tan: {tan}")
# degrees = float(input("Enter a degree: "))
# degree(degrees)

# Question 2
# Create a fully commented program to:
# Ask a user to input a word, and the program will check to see if the word is a palindrome (reads the
# same backwards and forwards).

# def palindrome(word):
#     rev = word[::-1]
#     if rev == word:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
# user_word = input("Enter a word: ")
# palindrome(user_word)

# Question 3
# Create a fully commented program to:
# Read in a first name and a surname from the keyboard and output in the format Surname, Initial e.g.
# Terry Gilliam becomes Gilliam, T (include the comma).
# The user should be able to repeat the process as many times as they wish.

# repeat = "y"
# while repeat.lower() == "y":
#     f_name = input("Enter your first name: ")
#     l_name = input("Enter your last name: ")
#     first_name = f_name[0].upper()
#     print(f"{first_name}, {l_name}")
#     repeat = input("Do you want to repeat the first letter? (y/n): ")
# print("Thank you for using this program")