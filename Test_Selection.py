from random import randint, random
from SelectionSort import selectionSort
from time import time

average= [randint(1,9999) for _ in range(999)]
best= sorted(average)
worst= sorted(average, reverse=True)
 
def test_Worst():
    start= time()
    assert selectionSort(worst,len(average)) == best
    print()
    print('.  Worst case =' + str(time()-start))
 
def test_Best():
    start= time()
    assert selectionSort(best,len(average)) == best
    print('   Best case =' + str(time()-start))
 
def test_Average():
    start= time()
    assert selectionSort(average,len(average)) == best
    print('Average case =' + str(time()-start))
