# Question 1
# What data type is each of the following?
# 7               = Integer
# 7.0             = Float
# “7”             = String
# True            = Boolean
# “False”         = String
# “????”          = String
# 16,000          = Integer
# 16.000          = Float
# 01698283100     = Integer
# 1 2 3           = Integer
# Use the type command with the inputs above to check your answers (some are tricky).
# If there’s an error, explain why and offer a solution.

# Question 2
# What would be displayed on the screen if you run each of these statements?
# a) print (2 + 3)        = 5
# b) print ("2 + 3")      = "2 + 3"
# c) print ("2" + "3")    = "23"
# Try typing each into PyCharm to see if you’re right. Explain what you get.
# If there’s an error, explain why and offer a solution.

# Question 3
# Is your Banner Number actually a number?
    # print(type("B01859436")) === str
# What about your mobile number?
    # print(type(+447345251553)) === int
    # print(type(07345251553)) === return an error as number cannot start with a 0

# Question 4
# Rewrite the Spam program using variables, allowing the user to choose how many tins of Spam they
# wish to buy
    # spam = 2.50
    # no_of_spam = int(input('How many spam do you want? ' ))
    # total_spam = spam * no_of_spam
    # print(f"You have brought {no_of_spam} tins of Spams")
    # print(f"Your total amount of spam is {total_spam}")

# Question 5
# Write a program which prompts for and reads in your name and age.
# The program should then output a message saying
# “Hello <your name>. You don’t look a day over <5 years less than your age>”
    # name = input('Enter your name: ')
    # age = int(input('Enter your age: '))
    # calc_age = age - 5
    # print(f"Hello {name}, You don't look a  day over {calc_age}.")