###################################################
##################################################
#functions 

#types of functions :
#1- standard library 
#2- user-defined 

# def  definition ():
   #code 
def greet(name):
    print ("hello " + name)

greet("ahmed")


def marioWall(number):
    for i in range(number):
        print("#")

marioWall(3)


def add (num1 , num2):
    sum = num1 + num2 
    print (sum)

add (5, 8)
################
def min (x ,y ):
    if x> y:
        print ( "x is bigger")
    else:
        print ("y is bigger")

min(5 ,6)