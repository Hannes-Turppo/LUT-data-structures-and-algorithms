# sales.py
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def sales(cars, customers):
    numberOfSales = 0
    quickSort(cars, 0, len(cars) - 1)
    for budjet in customers:
        current = None
        for i in range(len(cars)):
            if cars[i] > budjet:
                break
            current = i
        if current != None:
            cars.pop(current)
            numberOfSales += 1
        
    return numberOfSales


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))