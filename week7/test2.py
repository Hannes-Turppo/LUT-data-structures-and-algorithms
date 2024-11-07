permutation_count = 0

def permutations(k):
    global permutation_count
    if k == n:
        permutation_count += 1
        print(f"{permutation_count}: {numbers}")
    else:
        for i in range(1, n + 1):
            if not included[i]:
                included[i] = True
                numbers[k] = i
                permutations(k + 1)
                included[i] = False

# Example usage
if __name__ == "__main__":
    n = 5  # You can change this value to generate permutations of different lengths
    numbers = [0] * n
    included = [False] * (n + 1)
    permutations(0)
