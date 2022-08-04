from random import randint, random
import numpy as np
from MergeSort import mergeSort
from time import time

average= [randint(1,9999) for _ in range(999)]
best= sorted(average)
worst= sorted(average, reverse=True)
 
def test_Worst():
    start= time()
    assert np.array_equal(mergeSort(np.copy(worst), 0, len(average)-1), best)
    print()
    print('.  Worst case =' + str(time()-start))
 
def test_Best():
    start= time()
    assert np.array_equal(mergeSort(np.copy(best), 0, len(average)-1), best)
    print('   Best case =' + str(time()-start))
 
def test_Average():
    start= time()
    assert np.array_equal(mergeSort(np.copy(average), 0, len(average)-1), best)
    print('Average case =' + str(time()-start))