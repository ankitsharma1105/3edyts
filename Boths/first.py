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

# 2) Explain features of python program.

"""
1.Easy to Learn: Python has a simple syntax and is relatively easy to learn, making it a great language for beginners.

2.High-Level Language: Python is a high-level language, meaning it abstracts away many low-level details, allowing developers to focus on the logic of the program without worrying about memory management, etc.

3.Interpreted Language: Python code is interpreted line by line, making it easier to write and test code. This also means that Python code can be executed immediately, without the need for a separate compilation step.

4.Object-Oriented: Python is an object-oriented language, which means it organizes code into objects that contain data and functions that operate on that data.

5.Large Standard Library: Python has a vast and comprehensive standard library that includes modules for various tasks, such as file I/O, networking, and data structures.

6.Dynamic Typing: Python is dynamically typed, which means that the data type of a variable is determined at runtime, rather than at compile time.

7.Cross-Platform: Python can run on multiple operating systems, including Windows, macOS, and Linux.

8.Extensive Community: Python has a large and active community, with many online resources, libraries, and frameworks available.

9.Rapid Development: Python's syntax and nature make it ideal for rapid prototyping and development.

"""
# 3) Discuss difference between local and global variables.

'''
Local Variables   
zcs x2enywwcdvw
Defined inside our of system 
Defined within a specific block of code (e.g., a function)
Only accessible within that block
Created when the block is executed and destroyed when the block is exited

Global Variables

Defined outside of any block of code
Accessible from anywhere in the program
Created when the program starts and destroyed when the program ends

'''
# Global variable
x = 10

def my_function():
    # Local variable
    y = 20
    print("Local variable y:", y)

my_function()
print("Global variable x:", x)

# 4) Explain if – else statement with an example.

'''
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false'''
x = 5

if x < 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")

'''
In this example, the condition x > 10 is evaluated.
Since x is 5, which is less than 10, the condition is false. 
Therefore, the code in the else block is executed, and the output is:
x is less than or equal to 10

'''

# 5) What are fruitful function and void functions in python

'''
Fruitful Functions 
A fruitful function is a function that returns a value.
When a fruitful function is called, it performs some computation and returns a result,
which can be used by the caller. 
In other words, a fruitful function produces a value that can be used outside the function . 
Example:                                                                                       '''
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5 

'''
The add function takes two arguments, a and b, and returns their sum. 
The return statement is used to specify the value that the function should return.'''

'''
Void Functions 
A void function, on the other hand, is a function that does not return a value.
When a void function is called, it performs some action or side effect,
but it does not produce a value that can be used outside the function.   
Example:                                                                      '''
def greet(name):
    print("Hello, " + name + "!")

greet("Ankit")  # Output: Hello, Anki!
'''
The greet function takes a name argument and prints a greeting message to the console. 
It does not return a value. 
The function simply performs an action and then exits. '''

# 6) What are different ways to create strings in python .
'''
1>Single Quotes: You can create a string by enclosing text in single quotes '''
my_string = 'Hello, World!' 
'''
2>Double Quotes: You can also create a string by enclosing text in double quotes. '''
my_string = "Hello, World!" 
'''
3>Triple Quotes: Triple quotes are used to create a multiline string. You can use either single or double triple quotes. '''
my_string = """This is a
multiline string"""
'''
4>Raw Strings: Raw strings are created by prefixing the string with r. Raw strings treat backslashes as literal characters, rather than escape characters. '''
my_string = 'r'
'''
5>String Concatenation: You can create a string by concatenating multiple strings using the + operator. '''
my_string = 'Ankit, ' + 'Sharma'

# 7> Write a note on string slicing in python .
'''
A slice is a subset of a sequence (such as a string, list, or tuple) that is extracted from the original sequence using a specific syntax.
Slice is defined by three components:  
Start: The starting index of the slice (inclusive).
Stop: The ending index of the slice (exclusive).
Step: The increment between indices (default is 1).
syntax for a slice is: sequence[start:stop:step]    
example:                                                                            '''  
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
'''
Recursive function :
A recursive function is a function that calls itself in its own definition.
This allows the function to repeat its behavior until it reaches a base case that stops the recursion.
 
Advantages of recursive functions:
Recursive functions can be used to solve problems that have a recursive structure, such as tree or graph traversals.
They can be more intuitive and easier to understand than iterative solutions for some problems.
Recursive functions can be more concise and require less code than iterative solutions.

Example recursive function   '''
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

# 10> What are different type errors in python?
'''
1)TypeError: Python encounters an operation that is not supported for a particular data type. 
For example: '''                                                                                 
'''a = 5
b = "hello"
print(a + b)  # TypeError: unsupported operand type(s) for +: 'int' and 'str' '''

'''
2)AttributeError: This error occurs when you try to access an attribute that does not exist for an object. 
For example: '''
'''a = 5
print(a.append(10))  # AttributeError: 'int' object has no attribute 'append' '''

'''
3)IndexError: This error occurs when you try to access an index that is out of range for a sequence (such as a list, tuple, or string).
For example: '''
'''
a = [1, 2, 3]
print(a[5])  # IndexError: list index out of range '''

'''
4)KeyError: This error occurs when you try to access a key that does not exist in a dictionary.
For example:'''
'''
a = {"name": "John", "age": 30}
print(a["city"])  # KeyError: 'city'      '''

'''
5)SyntaxError: This error occurs when there is a syntax error in your Python code, such as a missing colon, incorrect indentation, or invalid syntax. 
For example: '''
if True :
    print("Hello")  # SyntaxError: invalid syntax

# 11> Write a bitwise operator in python.
'''
Bitwise AND (&)      
The bitwise AND operator (&) compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.   '''        

a = 5    # 101 in binary
b = 3    # 011 in binary

result = a & b  # 001 in binary
print(result)  # Output: 1

'''
Bitwise OR (|)
The bitwise OR operator (|) compares each bit of the first operand to the corresponding bit of the second operand. If either bit is 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.'''

a = 5    # 101 in binary
b = 3    # 011 in binary

result = a | b  # 111 in binary
print(result)  # Output: 7

'''
Bitwise XOR (^)
The bitwise XOR operator (^) compares each bit of the first operand to the corresponding bit of the second operand. If the bits are not the same, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.'''

a = 5    # 101 in binary
b = 3    # 011 in binary

result = a ^ b  # 110 in binary
print(result)  # Output: 6

'''
Bitwise NOT (~)
The bitwise NOT operator (~) inverts all the bits of the operand.'''

a = 5    # 101 in binary
result = ~a  # 010 in binary (two's complement representation)
print(result)  # Output: -6

'''
Left Shift (<<)    
The left shift operator (<<) shifts the bits of the number to the left and fills 0 on voids left as a result. The left shift operator essentially multiplies the number by 2 for each shift.'''

a = 5    # 101 in binary
result = a << 1  # 1010 in binary
print(result)  # Output: 10 

'''
Right Shift (>>)     
The right shift operator (>>) shifts the bits of the number to the right and fills 0 on voids left as a result. The right shift operator essentially divides the number by 2 for each shift. '''    

a = 10   # 1010 in binary
result = a >> 1  # 101 in binary
print(result)  # Output: 5

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


# 13. Write a short note on looping structure in python.
'''
In Python looping structure is used to execute a block of code repeatedly for a specified number of times. 
There are two main types of looping structures example loops and while loops.
For Loops
for loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence  
Syntax: for variable in sequence:
Example :  '''

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
 print(fruit) 

'''
While Loops 
while loop is used to execute a block of code as long as a certain condition is true.
Syntax: while condition:
Example:  ''' 
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
'''
parameterized function is a function that takes one or more arguments .
They make the code more flexible and reusable.
They allow us to write more concise and readable code.
They enable us to easily modify the function's behavior by changing the input parameters.

'''
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


#15. Explain any 5 math function in python with example. 
'''
1> abs(): Absolute Value  
The abs() function returns the absolute value of a number.
Ex :                                                              '''
x = 5
y = abs(x)
print(y)  # Output: 5
'''
2> pow(): Power 
The pow() function returns the value of a number raised to a power.
Ex :                                                                 ''' 
x = 10 
y = pow(x,2)
print(y)
'''
3> round(): Rounding 
The round() function returns the rounded value of a number.
Ex :                                                             '''
x = 3.14674523
y = round(x,3) 
print(y)
'''
4> max(): Maximum Value
The max() function returns the maximum value from a list of numbers.
Ex :                                                           '''
list = [1,2,3,4,5,6,7,8,9,10]
x = max(list)
print(x)

'''
5> math.sqrt(): Square Root
The math.sqrt() function returns the square root of a number.
Ex:                                                            '''
import math
x = 10000
y = math.sqrt(x)
print(y)

# 16. Explain the use if in and not in operator in with suitable program.
'''
in and not in operators are used to check if a value exists in a sequence (such as a string, list, or tuple) or not.

in Operator:
The in operator returns True if the value is found in the sequence, and False otherwise.             
Ex:                                                                                              '''
fruits = ['apple', 'banana', 'cherry']
if 'apple' in fruits:
    print("Apple is in the list")
else:
    print("Apple is not in the list")

# Output: Apple is in the list                                                                                                   

'''
not in Operator:
The not in operator returns True if the value is not found in the sequence, and False otherwise.
Ex:                                                                                                    '''
fruits = ['apple', 'banana', 'cherry']
if 'orange' not in fruits:
    print("Orange is not in the list")
else:
    print("Orange is in the list")

# Output: Orange is not in the list



# 17. The strings are immutable. Justify.
'''
1> Efficient memory usage
2> Thread safety
3> Code simplicity
''
Example 1: Attempting to modify a string                                                                   '''
''''my_string = "Ankit"
my_string[0] = "N"  # Trying to modify the first character
print(my_string)  # Output: "Ankit" (no change) '''
'''
we try to modify the first character of the string "Ankit" by assigning a new value to my_string[0].
Strings are immutable, the assignment has no effect, and the original string remains unchanged.

Example 2: Using the upper() method                                                             '''
'''my_string = "ankit"
new_string = my_string.upper()
print(my_string)  # Output: "ankit" (original string unchanged)
print(new_string)  # Output: "ANKIT" (new string created) '''

# 18. Explain string operations with an example. 
''''
1. Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: "Hello World"

2. Indexing
str1 = "Hello"
result = str1[0]
print(result)  # Output: "H"

3. Slicing
str1 = "Hello World"
result = str1[6:]
print(result)  # Output: "World"

4.Repetition
str1 = "Hello"
result = str1 * 3
print(result)  # Output: "HelloHelloHello"

5.String Formatting
Python provides several ways to format strings, including the % operator and the format() method.
name = "John"
age = 30
result = "My name is %s and I am %d years old." % (name, age)
print(result)  # Output: "My name is John and I am 30 years old."
'''

# 19. Explain the lower(), Split(), find(), len(), isdigit() function with example .
'''
lower():
 
Split(): substring create karna 

find():


len():

isdigit():

'''
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

