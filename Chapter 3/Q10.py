# Hand in

"""
Write a program that will compute MPG for a car. Prompt 
the user to enter the number of miles driven and the 
number of gallons used. Print a nice message with the 
answer.
"""

miles = float(input("How many miles have you driven?: "))
gallons = float(input("How many gallons have you used?: "))
print(f"You have {miles/gallons} mpg.")