###########################################
####################################################
#conditions 

age = 13 
if age > 20 : 
    print("you are too old")


score =int ( input())
passingScore = 50 
if score >= passingScore :
    print("you passed")

if score < passingScore : 
    print("you failed")


name = input("who are you : ")

if name == "the dog":
    print("oh no ! run")
elif name == "mickey":
    print("i love you")
else:
    print("you are safe")

############################################################

temp =float (input("temp : "))
hum = float (input ("hum : "))

if temp > 30 and hum < 50:
    print("it is hot")
else:
    print("it's fine")

###############################################################
money = int (input ("money "))

if money >= 3000:
    print("iam rich")
else:
    print("i am not rich")
