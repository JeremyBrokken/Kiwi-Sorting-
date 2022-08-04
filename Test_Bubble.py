from random import randint, random
from BubbleSort import bubbleSort
from time import time

average= [randint(1,9999) for _ in range(999)]
best= sorted(average)
worst= sorted(average, reverse=True)
 
def test_Worst():
    start= time()
    assert bubbleSort(worst) == best
    print()
    print('.  Worst case =' + str(time()-start))
 
def test_Best():
    start= time()
    assert bubbleSort(best) == best
    print('   Best case =' + str(time()-start))
 
def test_Average():
    start= time()
    assert bubbleSort(average) == best
    print('Average case =' + str(time()-start))
