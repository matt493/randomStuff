from math import ceil

def FindMinSticksAndWaste(stockLength, cuts):
    total_length = sum([count*length for count,length in cuts])
    sticks = ceil(total_length/stockLength)
    waste = sticks * stockLength - total_length
    return sticks, waste
# (count, length)
A = [(11, 1),(5,1),(10,1)]
print(FindMinSticksAndWaste(10, A))