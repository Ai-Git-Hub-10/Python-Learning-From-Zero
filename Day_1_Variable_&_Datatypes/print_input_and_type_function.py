# We used print function in python to display data
# It is pre-build function

print("Hello World")

print("I love my country.")

print("My name is Shayan Shah.")

# it will print all the content or strings inside Double quotes""
# print() function automatically add new line when call.

# Input function ():

# in python input( ) function is used for taking user_input or data 
# We simply write input() and first store it in a variable.
# it is also pre-build function.
# Input function by default always return string data.

name=input("Enter your name: ")
age=input("Enter your age: ")
print(name) # return any thing entered by user 


# Type function ():

# In python type() function is used to check the data type of varaible.
# We simply use  print(type(varaible))
print(type(name)) # output: class str

num = 3
print(type(num)) # output: class int

pi = 3.14 
print(type(pi)) # output: class flaot 

l = [1,2,3]
print(type(l)) # output: class list