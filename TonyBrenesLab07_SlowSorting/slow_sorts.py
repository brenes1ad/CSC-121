"""
slow_sorts.py -- the mighty (slow) triumvirate of basic sorts we study and occasionally use
   in our code.
A. Thall modified by Tony Brenes
CSC 121 W24
2/20/24
"""
import random

"""STUDENT: Selection sort works by taking the smallest element in the list, bringing it to the front, and then
    moving the beginning index forward one index as it considers everything moved to the start of the list sorted. 
    Everything after that beginning index is considered unsorted so it will be moved and sorted as needed."""
def selection_sort(arr):
    """sort the array elements from least to greatest"""
    #Always Order n**2 because it always swaps on every iteration
    #need to count comparisons
    #order n**2 comparisons but only order n swaps
    n = len(arr)
    compCount = 1
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if arr[least] > arr[j]:
                least = j
            compCount += 1
        arr[i], arr[least] = arr[least], arr[i]
    return compCount

"""STUDENT:  Insertion sort works by iterating through the list one element at a time and literally 
    inserting it where is belongs. It checks every item to it's left and if it's smaller, it shifts the larger
    elements to the right until it finds a number it's bigger than and it stops at that location. It moves the
    larger elements one spot to the right each time to make space for the sorting element to be inserted.
"""
def insertion_sort(arr):
    """sort the array elements from least to greatest"""
    #best case is order n
    #potentially n**2 comparisons and shifts
    n = len(arr)
    compCount = 1
    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            compCount += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return compCount


"""STUDENT: Bubble sort sorts a list by deciding whether or not the element and the one directly next to it need to 
swapped. It sorts left to right and check each element with the one to it's right and if the given element is larger
than the one on its right, it swaps. 
"""
def bubble_sort(arr):
    """Sort the array elements from least to greatest"""
    #best case is order n
    n = len(arr)
    swapCount = 0
    made_swaps = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                made_swaps = True
                swapCount += 1
        if not made_swaps:
            print("broke out early")
            break
    return swapCount

if __name__ == "__main__":
    n = 30
    arr1 = [ random.randint(0, n) for i in range(n) ]
    arr2 = list(arr1)
    arr3 = list(arr1)
    print("list =", arr1)
    comp1 = selection_sort(arr1)
    comp = insertion_sort(arr2)
    comp2 = bubble_sort(arr3)
    print("selection:", arr1)
    print("insertion:", arr2)
    print("bubble:", arr3)
    print("")
    print(f"insertion sort did {comp} comparisons")
    print(f"selection sort did {comp1} comparisons")
    print(f"bubble sort did {comp2} swaps")