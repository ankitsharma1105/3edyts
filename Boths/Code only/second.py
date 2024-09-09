# 1) Write a python program to calculate area of triangle and circle and print the result. Take input from user.

# Calculate area of triangle
'''
A = 1/2 b*h
'''
Base = float(input("Enter the base of the triangle :"))
Height = float(input("enter the height of the  triangle :"))
Are_of_triangle = 1/2 * Base * Height
print("The area of triangle is : " ,Are_of_triangle)

# Calculate area of circle
'''
A = πr2
'''
Radius = float(input("Enter the radius of the circle:"))
Area_of_circle = 3.14 * (Radius **2)
print("The area of the circle is: " , Area_of_circle)

# 3) Discuss difference between local and global variables.

# Global variable
x = 10

def my_function():
    # Local variable
    y = 20
    print("Local variable y:", y)

my_function()
print("Global variable x:", x)

# 4) Explain if – else statement with an example.

x = 5

if x < 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")

# 5) What are fruitful function and void functions in python

def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5 

def greet(name):
    print("Hello, " + name + "!")

greet("Ankit")  # Output: Hello, Anki!

# 7> Write a note on string slicing in python .

my_string = "hello world"
my_slice = my_string[0:5]  # start=0, stop=5, step=1
print(my_slice)  # Output: "hello"

# 8> Write a program to check if entered year is leap year or not .
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.") 

# 9> What is recursive function? Write its advantages. Explain with example

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

# 13. Write a short note on looping structure in python.

#for
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
 print(fruit) 

# while
 i = 0
while i < 5:
    print(i)
    i += 1

# break                       
for i in range(10):
   if i == 5:
    break
print(i)

#contineous
for i in range(15):
  if i ==10:
    continue
  print(i)

# 14. Write a short program to demonstrate the use of parameterized function .
 
 # parameters

def greet(name, age): 
    print(f"Hello, {name} You are {age} years old.")
# Call the function with arguments
greet("Ankit", 19)

 
def greet(student_Name, Rollno):
    print(f"Hello dear , your name is : {student_Name} and your rollno is : {Rollno} " )
greet("Ankit", 8)
greet("Karan", 9)
greet("Rishikesh", 10)

# 19. Explain the lower(), Split(), find(), len(), isdigit() function with example .

str1 = "ANKIT"
result = str1.lower()
print(result)

str2 = "ankit , kumar, sharma "
result = str2.split(",") 
print(result)

str3 = "Ankit Kumar Sharma"
result = str3.find("Sharma")
print(result)

str4 = "Ankit"
result = len( str4)
print(result)


str5 = "9876"
str = "ank123"
result = str5.isdigit()
digit= str.isdigit()
print(result)  # True 
print(digit)   # False

# 20. Explain any 10 string function with example. 

str1 = "ANKIT"
result = str1.lower()
print(result)

str2 = "sharma"
result = str2.upper()
print(result)

str3 = "ankit , kumar, sharma "
result = str3.split(",") 
print(result)

str4 = "Ankit Kumar Sharma"
result = str4.find("Sharma")
print(result)

str5 = "Ankit"
result = len( str5)
print(result)


str6 = "9876"
result = str6.isdigit()
print(result)  # True 

str7 = "ank123"
digit= str7.isdigit()
print(digit)   # False

str8 = "hello world"
result = str8.replace("world", "universe")
print(result)  # Output: "hello universe"

str9 = "hello world"
result = str9.startswith("hello")
print(result)  # Output: True

str10 = "hello world"
result = str10.endswith("world")
print(result)  # Output: True

# 21. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)

# Initialize an empty list to store the numbers

numbers = []

# Iterate over the range from 1500 to 2700 (both included)

for i in range(1500, 2700):

    # Check if the number is divisible by 7 and a multiple of 5

    if i % 7 == 0 and i % 5 == 0:

        # If the condition is true, add the number to the list

        numbers.append(i)

# Print the list of numbers
print("Numbers between 1500 and 2700 that are divisible by 7 and multiples of 5:")
print(numbers)

# 22. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    """
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Program")
    print("----------------------------")
    
    while True:
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# 23. Write a Python program to guess a number between 1 and 9.
import random

def guess_number():
    """
    Guess a number between 1 and 9
    """
    print("Think of a number between 1 and 9.")
    print("I'll try to guess it!")

    low = 1
    high = 9

    while True:
        guess = random.randint(low, high)
        print(f"Is your number {guess}?")

        response = input("Enter 'h' if my guess is too high, 'l' if it's too low, or 'c' if I'm correct: ")

        if response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1
        elif response == 'c':
            print("Yay! I guessed it!")
            break
        else:
            print("Invalid response. Please try again.")

if __name__ == "__main__":
    guess_number()
    3
    3
 # 24. Write a Python program that accepts a string and calculates the number of digits and letters.
def count_digits_and_letters(s):
    """
    Count the number of digits and letters in a string
    """
    digits = 0
    letters = 0

    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1

    return digits, letters

def main():
    s = input("Enter a string: ")
    digits, letters = count_digits_and_letters(s)

    print(f"The string contains {digits} digits and {letters} letters.")

if __name__ == "__main__":
    main()   

# 25. Write a Python program that checks whether a string represents an integer or not.
def is_integer(s):
    """
    Check if a string represents an integer
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    s = input("Enter a string: ")
    if is_integer(s):
        print(f"The string '{s}' represents an integer.")
    else:
        print(f"The string '{s}' does not represent an integer.")

if __name__ == "__main__":
    main()

# 12. Write a python program to display the following series.
''''

*
* *
* * *
* * * *
* * * * *                                                        '''
def print_staircase(n):
    """
    Print a staircase pattern of asterisks
    """
    for i in range(1, n + 1):
        print("* " * i)

# Test the function
print_staircase(5)
