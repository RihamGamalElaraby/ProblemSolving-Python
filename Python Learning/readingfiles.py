###################reading from files 

workersFile = open("data.csv" , "r")
print (workersFile.readable())
print (workersFile.read())
print (workersFile.readlines())



workersFile.close()
