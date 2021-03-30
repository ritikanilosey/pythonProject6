"""
Project: Mega Projects List - Find e to the Nth Digit
Problem: Just like the previous problem, but with e instead of Pi.
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go.
References: http://mathworld.wolfram.com/e.html; https://docs.python.org/2/library/decimal.html
"""
import decimal  # Use of decimal module due to increased precision compared to float()

factorial = 1  # The factorial is defined as 1 in order to find e from a nested series.

e = 2  # e is defined as 2 in order to begin the sequence of 2.xxxx.

for number in range(2, 50):  # The larger the range, the higher degree of accuracy for euler's number.
    # The two lines below perform the nested series calculation in order to find e.
    factorial *= number
    e += decimal.Decimal(1.0) / decimal.Decimal(factorial)

# Now that e has been calculated, the user can input the number of decimal places desired.

decimal_places = int(input("Please enter how many decimal places you would like returned for e: "))
while decimal_places > 20:
    print("Sorry, cannot compute fractional part greater than 20.")
    decimal_places = int(input("Please enter how many decimal places you would like returned for e: "))
else:
    print(str(e)[0:decimal_places + 2])
