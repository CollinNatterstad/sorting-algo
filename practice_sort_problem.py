#given an array of n integers find the smallest positive value not in the list
from random import randint

a =[]
for item in range(15):
    number = randint(1,100)
    a.append(number)


def solution1(a):

    sort_list = sorted(a)

    if max(sort_list) < 0:
        return 1
    
    elif max(sort_list) > 0:
        for number in range(1,max(a)):
            
            if number > 0 and number not in sort_list:
                return number

solution1(a=a)

def solution2(a):
    
    #this solution is one I found for this problem. It addresses the issue that I had previously. 
    #I couldn't figure out how to find the first object without looping through the entire list. 
    #this solution is simple and leverages the regular sort function in python.
    #in this way, we pass in the value of missing and modify it as we go. This returns the first value that is less than the item.

    #so for example, if missing was 5 and the next value is 6 the value is greater than 5 and we have our first blank value.  
    missing = 1
    for item in sorted(a):
        if item == missing:
            missing +=1
        
        elif item > missing:
            break

    print( missing)

solution2(a=a)
