#Library Import(s)
import numpy as np


#Import Kiwi Data and display
listKiwi = np.loadtxt(fname='C:\\jeremybrokken\\2022 Term 3\\1 Kiwi\Kiwi Data.txt',delimiter=",")
#print ("Unsorted data")
#print (listKiwi)

#Bubble Sort algorithm
def bubbleSort(listKiwi): #bubble sort function
    change = True #set change vairable

    while(change): #Run while loop while change is true
        change = False #if change remains false, will exit while loop

        for i in range(len(listKiwi) - 1): #Load next element to vairable
            if listKiwi[i] > listKiwi[i + 1]: #compare adjacent elements if first is larger
                listKiwi[i], listKiwi[i + 1] = listKiwi[i + 1], listKiwi[i] #swith elements if true
                change = True #repeats while loop as long as if statement is run
    return listKiwi

bubbleSort(listKiwi) #run bubble sort function

print("Bubble sorted data")
#print(listKiwi)