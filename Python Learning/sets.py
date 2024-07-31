###########################################
###########################################
#set

numbers = [1,2,3 ,4,5,6,7,8,9,10,10,10,12,1,4,5,9,12,13,14,15]
##################
uniqueList=[]

for i in numbers:
    if i not in uniqueList: 
        uniqueList.append(i)

print(uniqueList)

#######################
#sets مش بتقبل التكرار ، وبتستخدم ف ال unique numbers 
uniqueSet =set(numbers)
print (type(uniqueSet))
print (dir(uniqueList))

#all set
### ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
### '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
### '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
### '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
### '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 
### 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
################@@@@@@@@@