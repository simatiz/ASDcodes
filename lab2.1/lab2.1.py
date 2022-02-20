import random

def BubbleSort(array):
    n = len(array)
    amountcomparisons = 0
    amountswaps = 0
    for i in range(n-1):
        for j in range(n-1):
            amountcomparisons += 1
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                amountswaps += 1
    print("Length of array: ", n)
    print("Amount of swaps: ", amountswaps)
    print("Amount of comparisons: ", amountcomparisons, "\n")

def CombSort(array):
    n = len(array)
    step = n
    swapped = True
    amountcomparisons = 0
    amountswaps = 0
    while step > 1 or swapped:
        step = (step * 10) // 13
        if step < 1:
            step = 1
        swapped = False
        for i in range(0, n - step):
            amountcomparisons += 1
            if array[i] > array[i + step]:
                temp = array[i]
                array[i] = array[i + step]
                array[i + step] = temp
                swapped = True
                amountswaps += 1
    print("Length of array: ", n)
    print("Amount of swaps: ", amountswaps)
    print("Amount of comparisons: ", amountcomparisons, "\n")

print("Ordered sequence of elements (BubbleSort):")
array = list(range(1000))
BubbleSort(array)

print("Inverse ordered sequence of elements (BubbleSort):")
array = list(range(1000, 0, -1))
BubbleSort(array)

print("Random sequence of elements (BubbleSort):")
array = list(range(1000))
random.shuffle(array)
BubbleSort(array)

print("Ordered sequence of elements (CombSort):")
array = list(range(1000))
CombSort(array)

print("Inverse ordered sequence of elements (CombSort):")
array = list(range(1000, 0, -1))
CombSort(array)

print("Random sequence of elements (CombSort):")
array = list(range(1000))
random.shuffle(array)
CombSort(array)
