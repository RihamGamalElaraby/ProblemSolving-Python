#exception 





try:
    value = int(input('enter number '))
    print (value)
    result = 10 / 0 

except ZeroDivisionError:
    print('divide by zero')
except ValueError:
    print("error")






print('success') 