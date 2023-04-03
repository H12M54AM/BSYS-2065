"""
Range.py
Mar 29, 2023
Edward Naidoo
BCIT - BSYS 2065

Shows the difference between using one value for
the range or using two values...
"""

r1 = int(input("what is the single range? : "))

r2 = int(input("what is the first value? : "))
r3 = int(input("what is the second value? : "))

num = range(r1)
num2 = range(r2, r3)

print(f"Num: {num}")
for i in num:
    print(f"From num: {i}")

print()

print(f"Num2: {num2}")
for foo in num2:
    print(f"From num2: {foo}")
print()
