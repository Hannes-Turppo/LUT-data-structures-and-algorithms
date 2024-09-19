# finds valid splits in an array where all elements on the left are less than all elements on the right
# copilot suggested counting min and max values from left and right respectively for single pass execution.

def split(array):
    length = len(array)
    if length < 2:
        return 0
    
    # maximum values from left
    left_max = [0] * length
    left_max[0] = (array[0])
    for i in range(length):
        left_max[i] = max(left_max[i-1], array[i])

    # minimum values from right
    right_min = [0] * length
    right_min[-1] = (array[-1])
    for i in range(length - 2, -1, -1):
        right_min[i] = min(right_min[i+1], array[i])

    # count of valid splits
    count = 0
    for i in range(1, length):
        if left_max[i-1] < right_min[i]:
            count += 1

    return count



if __name__ == "__main__":
    print(split([1, 2, 3, 4, 5]))
    print(split([5, 4, 3, 2, 1]))
    print(split([2, 1, 2, 5, 7, 6, 9]))
    print(split([1, 2, 3, 1]))