# In This practice we will cover almost every concept about datatypes and master it.
# We will solve different problems practically to deeply understand what is important and how it works.
# We have different datatypes in python but we will discuss only basic , because in upcoming days we
# will cover all deeply a to z.

#---------------------------------------------------------#
# Practice problem 01:
# Taking inputs from user and print there types.
# We take input from user using input() function.

name = input ("Enter your name: ")
number = int(input("Enter number: "))   # int() is used to take only integer from user_input.
decimal = float(input("Enter the value of pi: "))        # float is used to take decimal datatype 

# Print all inputs and there datatypes:
# use type() function for checking data type.

print(name)
print(type(name))   # Class str

print(number)
print(type(number))     # Class int

print(decimal)
print(type(decimal))        # Class float

#------------------------------------------------------------#

# Practice problem 02:
# Take input as string convert it to int and float :

number = input ("Enter any number :")       # By default give string input.
print(number) 

# Convert input to integer datatype:
number = int(number)
print(number)
print(type(number))

# Convert input to float datatype :
number = float(number)
print(number)
print(type(number))

#----------------------------------------------------------------#

# Practice problem 03: 
# String lenght analyzer:

hospital_name = input ("Enter any hospital name to check its lenght:  ")

# We use len() function to find lenght of any string
# Its also count white spaces
print(hospital_name)
print(len(hospital_name))