#####################################
####################################
#loops 


print ( 5 * 3 + 2)
for i in range (0,5):
    print(i)

print(list(range(0,5)))
print(list(range(0,5,2)))

shopingList = ['watermelon' , 'orange' , 'cherry']

for i in (range(0 , len(shopingList))):
    print(shopingList[i])


for i in shopingList:
    if i == "orange":
         break
    print(i)

############################

numApple =0 
numOrange =0 

while True:
 fruit = input("what is the kind : ") 
 if fruit == "done":
    break
 elif fruit == "orange":
    numOrange += 1 
 elif fruit == "apple" :
    numApple += 1 
 else:
    print ("not valid")

totalFruit = numApple + numOrange 

print ("total : "  , totalFruit)


######################################3

friends = ['ali' , 'omar' , 'saad']
 
for i in range (0 , len(friends)):
    for j in  range (i+1 , len (friends)) :
        print(friends[i] + "and" + friends[j])
