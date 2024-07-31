###########################################################
###########################################################

# Lists in Python
# A list is a collection which can hold items of different data types and quantities.

# Creating a list with different types of data
friends = ["1", "code", True, False]
string = "this is my code "
list = (string.split())
print (list)


# Print the entire list
print(friends)

# Access the first element
print(friends[0])

# Access the last element
print(friends[-1])

# Access elements from index 1 to 2 (3 is not included)
print(friends[1:3])

# Access elements from index 1 to the end
print(friends[1:])

# Modify the first element
friends[0] = "reham"
print(friends[0])

# Creating another list
codee = ["programming", "python", "javascript", "tutorial"]
tutorial = ["extens", "lists1", "codee"]

# Create a shallow copy of the list
listNew = codee.copy()
print(listNew)

# Concatenate two lists
print(codee + tutorial)

# Extend the first list by appending elements from the second list
codee.extend(tutorial)
print(codee)

# Alternatively, you can use the += operator to extend the list
codee += tutorial
print(codee)

# Append a new element to the end of the list
codee.append("momen")
print(codee)

# Insert an element at a specific position
codee.insert(2, "roro")
print(codee)

# Remove a specific element
codee.remove("roro")
print(codee)

# Remove and return the last element
whatlast = codee.pop()
print(whatlast)
print(codee)

# Sort the list
codee.sort()
print(codee)

# Count the occurrences of an element in the list
count = codee.count("codee")
print(count)

# Clear the list (remove all elements)
codee.clear()
print(codee)



################ to do list
to_do_list = ["go to gym" , "do homework"]
print (to_do_list)