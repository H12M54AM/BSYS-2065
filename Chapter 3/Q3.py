"""
Question 3 

Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 

Write a Python program to solve the general version of the above problem. Ask the user 
for the time now (in hours), and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on the clock when the alarm goes off.
"""
# var hour
hour = 24

# var min
minute = 60

# var sec
seconds = 60

# Get time now
time_now = int(input("What is the time now? (In 24 hour clock): "))

# Get alarm time
alarm_time = int(input("When should the alarm go off? (In 24 hour clock): "))

# (13 + 50) % 24
print(f"It will be {(time_now + alarm_time) % 24}:00")