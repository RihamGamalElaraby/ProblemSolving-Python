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




# Inputs in Python 
name = input("Enter your name: ")
print("Hoi " + name)

