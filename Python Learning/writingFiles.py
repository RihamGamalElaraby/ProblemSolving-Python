#for workers in workersFile.readlines:
 #   print (workers)


workersFile = open("data.csv" , "a")
print (workersFile.writable())
workersFile.write(" \n rerere")
newfile = open ("newdata.csv" , "a")
newfile.write(" \n rerere")

# open("data.csv" , "a") #appesnd
# open("data.csv" , "r+") #read & write

 