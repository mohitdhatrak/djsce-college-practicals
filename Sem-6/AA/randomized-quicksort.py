import random

normal_count = 0
randomized_count = 0

def quick_sort(arr, first, last):
    global normal_count
    
    if first < last:
        normal_count += 1 # to count first < last comparison, when true
        end = partition(arr, first, last)
        quick_sort(arr, first, end - 1)
        quick_sort(arr, end + 1, last)
    else:
        normal_count += 1 # to count first < last comparison, when false
    
def partition(arr, first, last):
    # needed to tell function that scope of this variable needs to be considered as global
    global normal_count
    
    pivot = first
    i = first
    j = last
    
    while i < j:
        normal_count +=1 # to count i < j comparison, when true
        
        # i < n - condition needed to avoid index error
        while i < n and arr[i] <= arr[pivot]:
            i += 1
            normal_count +=1
        
        # j > 0 - condition needed to avoid index error
        while j > 0 and arr[j] > arr[pivot]:
            j -= 1
            normal_count +=1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            normal_count +=1

    normal_count += 1 # to count i < j comparison, when false
              
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

def randomized_quick_sort(arr, first, last):
    global randomized_count
    
    if first < last:
        randomized_count += 1 # to count first < last comparison, when true       
        end = randomized_partition(arr, first, last)
        randomized_quick_sort(arr, first, end - 1)
        randomized_quick_sort(arr, end + 1, last)
    else:
        randomized_count += 1 # to count first < last comparison, when false
        
def randomized_partition(arr, first, last):
    global randomized_count
    
    # randomly selecting the pivot
    pivot = random.randint(first, last)
    i = first
    j = last
    
    while i < j:
        randomized_count +=1 # to count i < j comparison, when true
        
        while i < n and arr[i] <= arr[pivot]:
            i += 1
            randomized_count +=1
        
        while j > 0 and arr[j] > arr[pivot]:
            j -= 1
            randomized_count +=1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            randomized_count +=1

    randomized_count += 1 # to count i < j comparison, when false

    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

# worst case for quicksort
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [8, 7, 6, 5, 4, 3, 2, 1]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)
print("No. of comparisons in quicksort:", normal_count)

# same case with randomized quicksort
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
randomized_quick_sort(arr, 0, n - 1)

print("Sorted array:", arr)
print("No. of comparisons in randomized quicksort:", randomized_count)
