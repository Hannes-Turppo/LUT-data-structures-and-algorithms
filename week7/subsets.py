# subsets.py


def subsets(n):
    def generate_subsets(index, current_subset):
        if index == n:
            subsetsOfN.append(current_subset[:])
            return
        # Include the current element
        current_subset.append(complete[index])
        generate_subsets(index + 1, current_subset)
        # Exclude the current element
        current_subset.pop()
        generate_subsets(index + 1, current_subset)

    subsetsOfN = []*0
    complete = list(range(1, n + 1))
    generate_subsets(0, [])
    subsetsOfN.sort()
    return subsetsOfN

if __name__ == "__main__":
    print(subsets(1))
    print(subsets(2)) 
    print(subsets(3)) 
    print(subsets(4)) 

    S = subsets(10)
    print(S[95])
    print(S[254])
    print(S[826])