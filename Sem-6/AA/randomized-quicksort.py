import random

normal_count = 0
randomized_count = 0

def quick_sort(arr, first, last, selected_pivots):
    global normal_count
    
    if first < last:
        normal_count += 1 # to count first < last comparison, when true
        end = partition(arr, first, last, selected_pivots)
        quick_sort(arr, first, end - 1, selected_pivots)
        quick_sort(arr, end + 1, last, selected_pivots)
    else:
        normal_count += 1 # to count first < last comparison, when false
    
def partition(arr, first, last, selected_pivots):
    global normal_count
    
    pivot = first
    selected_pivots.append(pivot)
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
              
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

def randomized_quick_sort(arr, first, last, selected_pivots):
    global randomized_count
    
    if first < last:
        randomized_count += 1 # to count first < last comparison, when true       
        end = randomized_partition(arr, first, last, selected_pivots)
        randomized_quick_sort(arr, first, end - 1, selected_pivots)
        randomized_quick_sort(arr, end + 1, last, selected_pivots)
    else:
        randomized_count += 1 # to count first < last comparison, when false
        
def randomized_partition(arr, first, last, selected_pivots):
    global randomized_count
    
    # randomly selecting the pivot
    pivot = random.randint(first, last)
    selected_pivots.append(pivot)
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

    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

# worst case for quicksort (asc or desc order)
# arr = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr = [i for i in range(1, 41)]
arr.reverse()
print("Initial array:", arr)

selected_pivots = []
n = len(arr)
quick_sort(arr, 0, n - 1, selected_pivots)
print("Sorted array:", arr)
print("Selected pivots:", selected_pivots)
print("Number of selected pivots:", len(selected_pivots))
print("No. of comparisons in quicksort:", normal_count)

# same case with randomized quicksort
arr = [i for i in range(1, 41)]
arr.reverse()
print("\nInitial array:", arr)

selected_pivots = []
n = len(arr)
randomized_quick_sort(arr, 0, n - 1, selected_pivots)
print("Sorted array:", arr)
print("Selected pivots:", selected_pivots)
print("Number of selected pivots:", len(selected_pivots))
print("No. of comparisons in randomized quicksort:", randomized_count)