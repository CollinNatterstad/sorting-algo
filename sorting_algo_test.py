from random import randint

'''This is NOT my work. I wanted to better understand common sorting methods and write out some implementations for coding interview practice.
This is provided by Santiago Valdarrama at Real Python who wrote a nice piece explaining the common factors.
I'm hosting this on my github repo simply for access away from home. This is simply educational. 

This article can be found here https://realpython.com/sorting-algorithms-python/#analyzing-the-strengths-and-weaknesses-of-bubble-sort

'''


#bubble sort super simple for a small array. 
#convenient because it is naively comparing the result of [i] to [i+1] directly to the right.

def bubble_sort(array):

    #establishes number of instances
    n = len(array)


    #for the length of n
    for i in range(n):
        alreay_sorted = True

        #start looking at teach item of the list one by one, 
        #comparing it with its adjacent value. With Each 
        #iteration, the portion of the array that you look at shrinks
        #becasue the remaining items have already been sorted.
        for j in range(n-i-1):
            
            #if value of array at j is less than the array directly to the write
            #swap the positions of the two options. 
            #each iteration runs from left to right. checking against the established criteria. 
            #this takes more time as each loop iteration requires complete run of the list. 
            #okay for simple and easy lists. Not as a great for expansive lists. 
            #runs through the list until all indexes [j] are < index [j+1]
            if array[j] > array[j+1]:

                array[j], array[j+1] = array[j+1],array[j]
                print(array,array[j])

                #changes flag to false so the loop continues. 
                already_sorted = False

        if already_sorted:
            break

    return array

#main idea is that the insertion list pushes smaller items to the left.
#j is reduced by 1 with each iteration of the while loop. 
# This allows the same index position to continue to move based on where in the ranking it falls.
# So this could be more convenient than bubble sorting and is typically faster as a result. 
def insertion_sort_non_tim(array):

    for i in range(1,len(array)):
        #setting variable to the value of array @ i.
        key_item = array[i]
        
        #creating new index varaible with j being 1 less than i.
        j = i-1
        
        #while j index is greater than zero and the value at array[j] is greater than key_item
        while j >= 0 and array[j] > key_item:
            #set array[j+1] equal to array[j]
            #shifts lesser value to the left. 
            array[j+1] = array[j]
            #reduces the count of j
            j-=1
            print(array)
        #this puts the key item in the correct place. So we start on the right and work left.
        array [j+1] = key_item

    return array


def merge(l_array,r_array):
    #this sort method operates on the divide and conquer method.
    #orginal input is broken down into several parts representing a sub problem.
    #each sub problem is solved recursively.
    #solutions of sub problems are combined together.
    #this requires two seperate function, the first function that works through the 

    #in this case, divides the list in half, and combines the results after

    #if length of left = 0 return right
    if len(l_array) == 0:
        return r_array

    #if length right = 0 return left
    if len(r_array) == 0:
        return l_array

    #creating an open result list/array
    result = []
    #setting index values equal to zero. external array splits the two evenly and goes index position by index position. 
    index_left = index_right = 0
    
    #while the length of the result array is less than the combined length of left and right...
    while len(result) < len(l_array)+ len(r_array):

        #if the left array @ left index is less than right array at right index. 
        if l_array[index_left] <= r_array[index_right]:
            #place that value in the result array
            result.append(l_array[index_left])
            #increase the index position by one
            index_left += 1

        else:
            #other wise append the right array value.
            result.append(r_array[index_right])
            #and increase right array index by one.
            index_right += 1

        #if index = to the length of the array, array is now empty.   
        if index_right == len(r_array):
            #add the remaining values if current index position and any value to it's index right.
            result += (l_array[index_left:])
            #exit the loop
            break 

        #if the left index = left array length
        if index_left == len(l_array):
            #add right array values of current index and right to the result array. 
            result += (r_array[index_right:])
            #and exit the loop
            break
    #return the result array
    return result

#this option splits the array, and creates the two seperate arrays to split. 
#faster and efficient for larger arrays. 
#not as fast as bubble sort or insertion short with smaller arrays.
#with big options it does provide best worst case scenario to divide the arrays. with O(nlog(base2)n)
def merge_sort(array):
    #if the array is less than one index just return what exists
    if len(array) < 2: 
        return array

    #utilizing floor division to evenly divide the array into two seperate arrays.
    # 
    midpoint = len(array) // 2

    #we are going to return the merge function until the list is combined and sorted.
    #this is going to call the list recursively.
    return merge(
        #left array = array to left of the midpoint as provided by the slice : notation
        l_array = merge_sort(array[:midpoint]),
        #right array = array to right of the midpoint as provided by the slice : notation
        r_array = merge_sort(array[midpoint:]))

#quick sort is going to operate on similar principles as merge sort. We are going to choose a random pivot point and create three buckets
#bucket one for values lower than pivot. bucket two for values equal to pivot, and bucket three for values greater than pivot.
#the problem with quick sort is which value is selected for the pivot value.
#if it is a median value it will be faster than if it is an end values require additional recursive trips to solve and more time as a consequence. 
#upside is that quick sort is usually very fast and very easy to run the segments in parrallel. It trades off memory though as recursion can be expensive. 
def quick_sort(array): 

    #if length is less than two. Just return the array as it has value of one. 
    if len(array) < 2:
        return array

    #creating our three buckets here
    low, same, high = [],[],[]

    #we are selecting an random integer from 0 to one less than the length of the array itself. 
    pivot = array[randint(0,len(array)-1)]

    #for the items in our list, 
    for item in array:
        #if item is less than pivot
        if item < pivot:
            #it goes in the low bucket
            low.append(item)
        #if item is equal to...
        elif item == pivot:
            #it goes in the same bucket
            same.append(item)
        #if item is greater than...
        elif item > pivot:
            #it goes in the high bucket
            high.append(item)

    #we are going to return the quick sort function for the high and low values and return the same values (as they are already in order.)
    #because this is a recursive call, the buckets get divided again and again and again until the base case is solved and the items are returned in the proper order!
    #that's pretty fucking cool. 
    return quick_sort(low) + same + quick_sort(high)


#this is the default method of sorting in python. It will take advantage of sequences of numbers that are already aligned and usually exist within the dataset.
#these are called 'natural runs'. This is accessible normally by utilzing the sort function. 
# we will start by modifying the initial insertion sort method
def insertion_sort_for_tim(array,left=0,right=None):

    if right == None:
        right = len(array)-1


    for i in range(left+1,right+1):
            #setting variable to the value of array @ i.
            key_item = array[i]
            
            #creating new index varaible with j being 1 less than i.
            j = i-1
            
            #while j index is greater than zero and the value at array[j] is greater than key_item
            while j >= left and array[j] > key_item:
                #set array[j+1] equal to array[j]
                #shifts lesser value to the left. 
                array[j+1] = array[j]
                #reduces the count of j
                j-=1
                print(array)
            #this puts the key item in the correct place. So we start on the right and work left.
            array [j+1] = key_item

    return array


def tim_sort(array):
    min_run = 32
    n = len(array)

    for i in range(0,n,min_run):
        insertion_sort_for_tim(array=array,n=i,left= min((i+min_run-1)), right = n-1)

    size = min_run
    while size < n:

        for start in range (0,n,size*2):
            midpoint = start + size - 1
            end = min((start + size*2 - 1),(n-1))

        merged_array = merge(left = array[start:midpoint +1]
        ,right = array[midpoint+1:end+1])

        size *= 2

    return array

array = [2,1,9,8,2,7,5,7,2,3,4,8]

sorted = tim_sort(array=array)
print(sorted)