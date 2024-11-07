# made entirely by copilot to test the quicksort algorithm

pivot_count = 0

def quicksort(arr, pivot_strategy='first'):
    global pivot_count
    if len(arr) <= 1:
        return arr

    pivot = choose_pivot(arr, pivot_strategy)
    pivot_count += 1
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(less, pivot_strategy) + equal + quicksort(greater, pivot_strategy)

def choose_pivot(arr, pivot_strategy):
    if pivot_strategy == 'first':
        return arr[0]
    elif pivot_strategy == 'middle':
        return arr[len(arr) // 2]
    elif pivot_strategy == 'last':
        return arr[-1]
    else:
        raise ValueError("Invalid pivot strategy. Choose 'first', 'middle', or 'last'.")

# Example usage
if __name__ == "__main__":
    array = [14,1,2,6,11,8,5,9,4,3,10,7,12,13]
    print("Original array:", array)
    
    pivot_count = 0
    sorted_array = quicksort(array, 'first')
    print("Sorted array with first element as pivot:", sorted_array)
    print("Number of pivots used:", pivot_count)
    
    pivot_count = 0
    sorted_array = quicksort(array, 'middle')
    print("Sorted array with middle element as pivot:", sorted_array)
    print("Number of pivots used:", pivot_count)
    
    pivot_count = 0
    sorted_array = quicksort(array, 'last')
    print("Sorted array with last element as pivot:", sorted_array)
    print("Number of pivots used:", pivot_count)