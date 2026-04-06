# Its is a practice file on varaibles solve different problems to understand the concepts practically.
# This practice session cover almost every concept on variable.

# Creating Smart profile builder 

# Student Info


name = "Shayan Shah"  #String
age = 23        #Integer
hieght = 5.9    #FLoat 
is_student = True   #Boolean

#Print all info
print("+++ STUDENT INFO CARD +++")
print("The student name =",name)
print("He is",age,"year old.")
print("His hieght =",hieght)
print("He is a student =",is_student)

#------------------------------------------------------#

# Practice problem 2:
# Swapping values:

a = 20
b = 30

print(a,b)  # print 20 , 30

# now swap them

a  , b = b , a
print(a,b)  # print 30 , 20

#-------------------------------------------------------#

# Practice problem 3:
# Update present varaible:
# First creat a variable then update it 

age = 23
print(age)      # print 23

# Update value of age by 5
# simply (+) operator to add or update a variable value

updated_age = age + 5
print(updated_age)      # print 28

#--------------------------------------------------------#

# Practice problem 4:
# Multiple assiagnment.
# Multiple assignment at single line.

a , b , c = 10 , 20 , 30 
print(a,b,c)    # print 10 , 20 , 30 

# Swapping :

a , b , c = b , c , a # print 20 , 30 , 10 
print(a,b,c)

#---------------------------------------------------------#

# Practice problem 5:
# Dynamic typing 
# Use type() function to check its type

data = 100 
print (data)
print(type(data)) # integer type

# Both output will be same but having different data types

data = str(data)
print (data)  
print(type(data))   # string type

#---------------------------------------------------------#

# Practice problem 6:
# Copying and reference

a = 40
b = a       # Copying a to b

print(a,b)  # print 40 , 40 

# update variable

a = 60 
print(a)        # print 60
print(b)        # print 40

#----------------------------------------------------------#

# Practice problem 7:
# Take input from user 
# Using input function
# Asking name and favorite color store it and display it

name = input ("Enter your name: ")
favorite_color = input ("Enter your favorite color name: ")

print("Your name is : ",name)       # display user input e.g. jhon
print("Your favorite color is : ",favorite_color)       # display input e.g Black

#-----------------------------------------------------------#

# Practice problem 8:
# Adding two variables

first_name = input ("Enter your first name: ")
last_name = input ("Enter your last name: ")

full_name = first_name +" "+ last_name

print("Your name is = ",full_name) # display full_name of user e.g. Thomas shelby