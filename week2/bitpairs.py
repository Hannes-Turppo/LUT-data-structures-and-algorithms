# Finds distances betwen all bit pairs in a string of 1s and 0s

def pairs(bit_string):
    total_distance = 0
    count_of_ones = 0
    sum_of_positions = 0
    
    for i, bit in enumerate(bit_string):
        if bit == '1':
            total_distance += (count_of_ones * i - sum_of_positions)
            
            count_of_ones += 1
            sum_of_positions += i
    
    return total_distance


if __name__ == "__main__":
    print(pairs("100101"))
    print(pairs("101"))
    print(pairs("100100111001"))