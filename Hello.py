print('hello')
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
# Function to check if a number is even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Taking user input
num = int(input("Enter a number: "))

# Checking if the number is even
if is_even(num):
    print(num, "is an even number.")
else:
    print(num, "is not an even number.")
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Taking user input
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

