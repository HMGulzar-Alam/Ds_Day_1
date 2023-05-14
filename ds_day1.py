# -*- coding: utf-8 -*-
"""DS_Day1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e_nWbF8oWHMcVs0X-zw3IHm3SR2DNPMY
"""



"""1. **Python Output**"""

print(True)

print("Hello World")

print("Salman Khan")

print(Salman khan)

print("Bhaio", 123,True, sep = "/")

print("Hello", "World", sep = '-')

print("Hello", end = " ")
print("world")



"""##2. Data Types"""

#Integer
print(8)

#1e309
print(1e309)

#Decimal/float
print(1.76)
print

print(True)
print(False)

#Text/String
print("Assalam o Alaikum")

# complex
print(5+6j)

# List -> C -> Array
print([1,2,3,4,5])

# Tuple
print((1,2,3))

# Set
print({1,2,3})

# Dictionaries
print({'Name':'Gulzar', 'Roll No':12})
print({"Name": "Adil", "Roll No": 13})

#type
type([1,2,3])

#Variable

name = "Gulzar"
print(name)

a  = 5
b = 6
print(a + b)

# Dynamic -> automatically understand what kind of value python variable have
a = 5

# static 
# int a = 5

# Dynamic binding -> Variables value change as per requirements
a  = 10
print(a)

a = 'Gulzar'
print(a)

#static binding -> The value does not change if any condition
# int a = 10

# python intelligent
a = 1
b = 2
c = 12
print(a,b,c)

a,b,c = 2,4,6
print(a,b,c)

a=b=c = 5
print(b)



"""### Comments



"""

# comment

# Kayword -> basically predefined word in every language 
# like : as, if, is, in


# Identifiers -> basically we will create it or edit it, and can not starting with digits or special character
first_name = "Gulzar"
Second_name = "Alam"
print(first_name, Second_name)
print(first_name + Second_name)

# identifiers can not be keyword

# static (remain same) vs Dynamic (real time changes)
input("Enter your good name ")

# Example of dynamic
first_number = input("Enter first number  ")
second_number=input("Enter second number  ")
print(type(first_number), type(second_number))

# add two number
sum = first_number + second_number
print(sum)

# Type conversion

# implicit (interpreter solve itself and find which type of data type ) vs explicit (programmer request to python to change the data type)

# example of implicit
print(5 + 5.5)
print(type(5), type(5.5))

print(5 + "5")

#explicit has builtin function like: str, int

# str -> int
print("4")

#requested to program to change data type

type(int('4'))

# int -> str
str(5)

# Example
# 1. take input from users and stored them in variable
fnum = input("Enter first number: ")
snum = input("Enter second number: ")

# add the two number
sum = int(fnum) + int(snum)
print(sum)
print(type(fnum))

# Literals
a = 0b1010 #Binary literal
print(a)

b = 100
print(b) #Decimal literals

c = 0o310 #octal literals
print(c)

d = 0x12c #Hexa Decimal
print(c)

# Operators
# 1.Arithmetic
# 2. Logical 
# 3. Assignment
# 4. Bitwise
# 5. Relational
# 6. Membership

#Float literals

float_1 = 1.5
float_2 = 1.5e2 #1.5 x 10^2
float_3 = 1.5e-2

print(float_1, float_2, float_3)

#Complex literals
a = 3.14j
print(a.real, a.imag)

# Python String

string = 'This is python'
strings = "This is python"
char = 'C'
unicode = u"\U0001f600"
raw_data=r"raw \n string"

print(string)
print(strings)
print(char)
print(unicode)
print(raw_data)

a = True + 1
b = False - 1

print("a:" , a)
print("b:" ,  b)

a = None
print(a )



"""In python no way to using variable declared in python"""

k
a = 10
b = 20
print(a,b,k)

k = None
a = 10
b = 20





