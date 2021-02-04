currentyear = int(input('Enter the year you wish to begin counting from. Use astronomical year numbering. '))

def isLeap(currentyear):
 
    if currentyear % 4 != 0:
        return False
    elif currentyear % 100 != 0:
        return True
    elif currentyear % 400 != 0:
        return False
    else:
        return True

next20 = []
x = 0
while x < 20:    
    if isLeap(currentyear) == True:
        next20.append(currentyear)
        x += 1
    currentyear += 1
    
print(next20)
