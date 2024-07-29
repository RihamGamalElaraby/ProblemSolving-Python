######################################################################
######################################################################
## Libraries

from math import *

######################################################################
######################################################################

# Variables 
charachter_name = "mourad"  
age = "50"
isRight = True 

# Print statements to display the character's name and age
print("the name is " + charachter_name + " GOOD!") 
print("his age is " + age + " so young!")  

#########################################################################
########################################################################

# Strings used in plain text & strings 

# Print a simple string
print("rehaaaaaaaam") 

# Use special characters like \n for newline, \" for double quotes, \\ for backslash, and \t for tab
print("rehaaa \n aaaaam") 

# Concatenate strings using the + operator
text = "hi this concatenation"
print(text + " rehaaa \n aaaaam") 

# String functions
print(text.lower())         # Convert to lowercase
print(text.upper())         # Convert to uppercase
print(text.isupper())       # Check if all characters are uppercase
print(text.islower())       # Check if all characters are lowercase
print(text.lower().isupper()) # Convert to lowercase then check if all characters are uppercase (should return False)
print(len(text))            # Get the length of the string
print(text[0])              # Get the first character of the string
print(text.index("con"))    # Find the index of the substring "con"
print(text.replace("con", "bon")) # Replace "con" with "bon"

#########################################################################
########################################################################

# Numbers in Python
print(1)
print(0.55)
print(-55)
print(1 - 1) 
print(3 + 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)

# Working with variables and numbers
my_num = 5 
print(my_num)
print(str(my_num))           # Convert number to string
print(str(my_num) + " my favourite num") # Concatenate string with number
print(float(my_num))         # Convert number to float
print(abs(my_num))           # Get the absolute value
print(pow(2, 3))             # Calculate 2 to the power of 3
print(max(2, 3, 4, 5))       # Find the maximum value
print(min(2, 3, 4, 5))       # Find the minimum value
print(round(3.4))            # Round the number
print(floor(3.4))            # Get the floor value
print(ceil(3.4))             # Get the ceiling value
print(sqrt(16))              # Calculate the square root

#########################################################################
########################################################################

# Inputs in Python 
name = input("Enter your name: ")
print("Hoi " + name)

