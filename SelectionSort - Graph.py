#Library Import(s)
import numpy as np
import matplotlib.pyplot as plot

#Import Kiwi Data and display
listKiwi = np.loadtxt(fname='C:\\jeremybrokken\\2022 Term 3\\1 Kiwi\\Kiwi Data.txt',delimiter=",")
listCopy = np.copy(listKiwi)
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

xAxis = [0] * (len(listCopy))
for i in range(len(listCopy)):
    xAxis[i] = i

# # Unsorted Data Displayed on Graph
plot.figure(1)
plot.title('Unsorted - Kiwi Weights')
plot.yticks(np.arange(min(listCopy),max(listCopy),0.5))
plot.scatter(xAxis, listCopy)
plot.ylabel('KG')
plot.xlabel('#Kiwi')

# Sorted Data Displayed on Graph
plot.figure(2)
plot.title('Sorted - Kiwi Weights')
#plt.yticks(np.arange(min(selectionSort),max(selectionSort),0.5))
plot.scatter(xAxis, listKiwi)
plot.ylabel('KG')
plot.xlabel('#Kiwi')
plot.show()
