#Exercise 1

#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

num=str(input("Enter any two digit number: "))

print(f"{int(num[0])} + {int(num[1])} = {int(num[0])+int(num[1])}")

#Exercise 2

"""Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers."""

age=int(input("Enter your age: "))
a=int(90)-age
days=int(a)*int(365)
weeks=int(a)*int(52)
months=int(12)
print(f"you have {days} days, {weeks} weeks and {months} months left.")

#Exercise 3

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
"""
The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

"""
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
BMI=weight//(height**2)
print(f"weight = {weight}")
print(f"height = {height}")
print(f"BMI = {round(BMI)}")

#Exercise 4

# CAPSTONE PROJECT

"""
# TIP CALCULATOR

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is  30.00and 3.60 tip.

"""

print("Welcome to tip calculator!")
total_bill=float(input("What is the total bill?\n"))
tip=float(input("How much tip would you like to give (in %)?\n"))
no_of_people=int(input("How many people to split the bill?\n"))
total_bill_with_tip=total_bill+(total_bill*(tip//100))
each_contribution=total_bill_with_tip//no_of_people
print(f"Each person should pay: {each_contribution}")



