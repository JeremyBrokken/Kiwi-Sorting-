#Library Import(s)
import numpy as np

#Import Kiwi Data and display
listKiwi = np.loadtxt(fname='C:\\jeremybrokken\\2022 Term 3\\1 Kiwi\\Kiwi Data.txt',delimiter=",")
#print ("Unsorted data")
#print(listKiwi)

#merge = assaigns sorted data into array
def merge(array, left, mid, right):

    #define important vairables
    leftLength = mid - left + 1 #length of left divide
    rightLength = right - mid #lenght of right divide
    leftArray = [0] * (leftLength) #temp left array
    rightArray = [0] * (rightLength) #temp right array
 
    #Load real data(array) into left and right array
    for i in range(0, leftLength): 
        leftArray[i] = array[left + i]
    for j in range(0, rightLength):
        rightArray[j] = array[mid + 1 + j]
 
#reset vairables and assaign left o k
    i = 0; j = 0; k = left

#assaign sorted data into original array
    while i < leftLength and j < rightLength:
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1
 
    # if remaining left copy to array
    while i < leftLength:
        array[k] = leftArray[i]
        i += 1
        k += 1
 
    # if remaining right copy to array
    while j < rightLength:
        array[k] = rightArray[j]
        j += 1
        k += 1
 
#merge sort = recursively splits data array
def mergeSort(array, left, right):
    if left < right: #condition = if left is less than right
        mid = left+(right-left)//2 #assigns middle
 
        mergeSort(array, left, mid) #left divide
        mergeSort(array, mid+1, right) #right divide
        merge(array, left, mid, right) #left, right and mid assigned and sent to merge function
    return array
 
sorted = mergeSort(np.copy(listKiwi),0,len(listKiwi)-1) #run merge sort and load array to vairable
print("Merge sorted Data is")
#print (sorted)