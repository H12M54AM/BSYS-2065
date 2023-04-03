# Needs work
# hand in
"""
It is possible to name the days 0 through 6 where day 0 
is Sunday and day 6 is Saturday. If you go on a 
wonderful holiday leaving on day number 3 (a Wednesday) 
and you return home after 10 nights you would return 
home on a Saturday (day 6) 

Write a general version of the program which asks for 
the starting day number, and the length of your stay, 
and it will tell you the number of day of the week you 
will return on.
"""

days = ["Sunday", "Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday"]

starting_day = int(input("What is the starting day? : "))
days_num = int(input("How many days are you going for? : "))


"""
Statement checks if the users days_num is realistic
"""
if days_num > len(days):
    print(days[int((starting_day + days_num)) - len(days)])
elif days_num < len(days) | starting_day < len(days):
    print("Don't even try to time travel bud...")
else:
    print(days[starting_day + days_num])