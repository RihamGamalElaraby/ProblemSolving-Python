###########################################
######################################
#  MadLibs game 

#embedding strings

color = input("please enter a color : ")
plural_noun = input("please enter a plural_noun : ")
adj = input("please enter a adj : ")

print ("trees are "  + color)
print (plural_noun + " are mean")
print ("please keep it " + adj)

email = "Dear %s , you have an exam tomorrow \n thank you ;" 
name = input("what is your name:  ")
mr = "mr . salah"
mul_string = mr * 5
print (email % name + mr)
print (mul_string)