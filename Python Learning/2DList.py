#2d lists  

no_list = [
[ 1,2,3,4 ] ,
[ 5,6,7,8 ] ,
[9,10,11,12] ,
[13,14,15,16],
[0],
]

print (no_list[1][2]) 


#nestedloops

for row in no_list:
    for col in row:
     print(col)