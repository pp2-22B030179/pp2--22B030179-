
#2
if 5 > 2:
    print("Five is greater than two!")
#3
#This is a comment
#4
"""
This is a comment
written in 
more that just one line
"""
#5
carname = "Volvo"
#6
x=50
#7
x=5
y=10
print(x+y)
#8
x = 5
y = 10
z= x + y
print(z)
#9
myfirst_name = "John"
#10
x=y=z="Orange"
#11
def myfunc():
  global x
  x = "fantastic"
#12
x = 5
print(type(x))

int
#13
x = "Hello World"
print(type(x))

str
#14
x = 20.5
print(type(x))

float
#15
x = ["apple", "banana", "cherry"]
print(type(x))

list
#16
x = ("apple", "banana", "cherry")
print(type(x))

tuple
#17
x = {"name" : "John", "age" : 36}
print(type(x))

dict
#18
x = True
print(type(x))

bool
#19
x = 5
x = float(x)
#20
x = 5.5
x = int(x)
#21
x = 5
x = complex(x)
#22
x = "Hello World"
print(len(x))
#23
txt = "Hello World"
x = txt[0]
#24
txt = "Hello World"
x = txt[2:5]

#25
txt = " Hello World "
x = txt.strip()

#26
txt = "Hello World"
txt = txt.upper()
#27
txt = "Hello World"
txt = txt.lower()
#28
txt = "Hello World"
txt = txt.replace("H", "J")
#29
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#30
print(10 > 9)

True
#31
print(10 == 9)

False
#32
print(10 < 9)

False
#33
print(bool("abc"))

True
#34
print(bool(0))

False
#35
print(10 *5)
#36
print(10/2)
#37
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
#38
if 5 !=10:
  print("5 and 10 is not equal")
#39
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
#40
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#41
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
