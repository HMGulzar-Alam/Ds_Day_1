# -*- coding: utf-8 -*-
"""Day_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1thIC70Emni3v9RgGocUPxQSCB3Jn-Igb

Sequence sum
1/1!+2/2!,...
"""

# factorial
n = int(input("Plz enter number: "))

fact = 1
result = 0
for i in range(1, n+1):
  fact = fact*i
  result = result + i/fact
  print(result)

"""# Nested loop"""

# code here

for i in range(1,5):
  for j in range(1,5):
    print("*")
    print(i,j)

# # code
# rows = int(input("plz enter number of rows"))
# for i in range(1, rows+1):
#   for j in range(1, i+1):
#     print("*", end='')
#     print()

rows = int(input("plz enter number of rows"))
for i in range(1, rows+1):
  for j in range(1, i+1):
   print("*", i,j,end='')
   print()

# code here
rows = int(input("Plz enter number: "))
for i in range(1, rows+1):
  for j in range(1, i+1):
    print(j, end='')
  for k in range(i-1,0,-1):
    print(k, end='')  
    print()



"""#Loop Control Statement
1.Break
2.Continue
3.pass
"""

for i in range(1,5):
  if i == 5:
    break
    print(i)

# code for prime number

lower = int(input("Plz enter lower range"))
upper = int(input("plz enter upper range"))

for i in range(lower, upper+1):
  for j in range(2, int(i/2)+1):
    if i%j == 0:
      break
    else:
      print(i)

#pass

for i in range(1,10):
  if i == 5:
    pass
    print(i)

# continue
for i in range(1,10):
  if i==5:
    continue
    print(i)

"""String are sequence of characters
1.Creating string
2. accessing string
3. chars to string
4. Editing on string
5. Deleting string
6. operation on string
7. String function
"""

# Creating string

a = 'its bat'
print(a)

b = "its bat"
print(b)

c = '''its bat'''
print(c)

# accessing positive substring from chars

name = "adil bhai"
print(name[2])

# accessing Negative substring from chars
name = "khan"
print(name[-2])

# slicing
a = "javed Khan"
print(a[0:5])

# slicing with jump
a = "javed Khan"
print(a[0:8:2])

# negitive slicing
a = "javed khan"
print(a[::-1])

b = "Hello world"
print(b[-5:])

c = 'hello world'
print(c[-1:-6:-1])

# Editing and Deleting string
s = "hello_word"
s[0]="a"

del s[-1:-5:2]

# python string is immutable

"""Operation on strings
1.Arithmetic
2.Realational
3.Logical
4.Loops on string
5.Membership Operations
"""

# 1. Arithmetic Operation
print("Karachi"+ " " + "Lahore")

print("Karachi"*5)

print("*"*5)

# 2. Relational
"karachi" > "lahore"

"lahore" > "karachi"
# lexiographically means ascii code base

# 3.Logically

" " and "world"

# " " or "world"



not "hello"

for i in 'khan':
  print(i)

for i in "Quetta":
  print("karachi")

# Common functions in python
# 1.len
# 2.Max
# 3.Min
# 4.sorted

len("hello world")

max("hello world") #count on the behalf of ascii values

min("hello world") #count on the behalf of ascii values

sorted("hello_world") #count on the behalf of ascii values

"""Capitalize/Upper/Lower/Title/swapcase"""

a = "khan javed"
print(a.capitalize())
print(a.title())

"hello world".lower()

"paistan".upper()

"Karachi Quetta".swapcase()

"""# Count / Find / Index
"my name is khan".count("n")

"my name is khan".find("is")

"my name is khan".index("e")
"""

# Endswith/Startswith

"my name is khan".startswith("my")
"my name is khan".endswith("my")

# Format

name = input("plz enter your name: ")
age = input("plz enter age: ")

'My name is {} and i am {} years old'.format(name,age)

# islaphanum/isalpa/isdigit/isidentifier

'khan123'.isalnum()

"khan123".isalpha()

"123".isalnum()

"data1".isidentifier()

# split/join

print("my name is khan".split("is"))

print("my name is khan".join("."))

# replace
print("my name is khan".replace("khan", "adil"))

# strip
"khan                     ".strip()

