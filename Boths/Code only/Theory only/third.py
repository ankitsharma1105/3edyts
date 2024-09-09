# 2) Explain features of python program.

'''
1.Easy to Learn: Python has a simple syntax and is relatively easy to learn, making it a great language for beginners.

2.High-Level Language: Python is a high-level language, meaning it abstracts away many low-level details, allowing developers to focus on the logic of the program without worrying about memory management, etc.

3.Interpreted Language: Python code is interpreted line by line, making it easier to write and test code. This also means that Python code can be executed immediately, without the need for a separate compilation step.

4.Object-Oriented: Python is an object-oriented language, which means it organizes code into objects that contain data and functions that operate on that data.

5.Large Standard Library: Python has a vast and comprehensive standard library that includes modules for various tasks, such as file I/O, networking, and data structures.

6.Dynamic Typing: Python is dynamically typed, which means that the data type of a variable is determined at runtime, rather than at compile time.

7.Cross-Platform: Python can run on multiple operating systems, including Windows, macOS, and Linux.

8.Extensive Community: Python has a large and active community, with many online resources, libraries, and frameworks available.

9.Rapid Development: Python's syntax and nature make it ideal for rapid prototyping and development.'''

# 3) Discuss difference between local and global variables.

'''
Local Variables   

Defined inside our of system 
Defined within a specific block of code (e.g., a function)
Only accessible within that block
Created when the block is executed and destroyed when the block is exited

Global Variables

Defined outside of any block of code
Accessible from anywhere in the program
Created when the program starts and destroyed when the program ends '''

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