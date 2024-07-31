def power(baseNum , powerNum):
    result = 1
    for index in range(powerNum):
        result = result * baseNum
    return result

print(power(2,2))
    