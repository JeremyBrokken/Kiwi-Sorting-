#Library Import(s)
import numpy as np

#Import Kiwi Data and display
listKiwi = np.loadtxt(fname='C:\\jeremybrokken\\2022 Term 3\\1 Kiwi\\Kiwi Data.txt',delimiter=",")
#print ("Unsorted data")
#print (listKiwi)

#selection sort function
def selectionSort(array, size): #selection sort function
    for xSS in range(size): #Load next element to vairable
        minSS = xSS #smallest elememt holder, starts with initial element
        for iSS in range(xSS + 1, size): #load every element after initial element
            if array[iSS] < array[minSS]: #compare is new element is smaller that current
                minSS = iSS # Loads element to smallest holder if true
        (array[xSS], array[minSS]) = (array[minSS], array[xSS]) #when all elements are checked, the smallest is swapped with the initial element
    return array

selectionSort(listKiwi, len(listKiwi)) #run function

print("Selection sorted Data is")
#print(listKiwi)