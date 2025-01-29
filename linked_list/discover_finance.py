# def getMinOperations(computationalTime):
#     # totalOperations = 0
#     track_operations = []
    
#     for time in computationalTime: # 2 --> 4 --> 8
#         if time % 2 == 0: #, 2%2 = 0, 4%2 = 0, 8%2 = 0, 
#             totalOperations = 0 

#             while time % 2 == 0: # 2/2, (4/2,2/2,), (8/2,4/2,2/2)
#                 time //= 2
#                 totalOperations +=1 # 3
#             track_operations.append(totalOperations) #[1,2,3,4]
#     return max(track_operations)


def getMinOperations(computationalTime):
    computationalTime.sort(reverse=True)  # Start with the largest numbers
    operations = 0
    seen = set()  # Track numbers we've already processed
    
    for num in computationalTime:
        if num % 2 == 1:
            continue  # Skip odd numbers

        # If we've already processed this even number, skip it
        if num in seen:
            continue

        # Process this even number
        current = num
        while current % 2 == 0:
            seen.add(current)  # Mark this number as processed
            current //= 2
            operations += 1  # Count the division

    return operations


print(getMinOperations([6, 2, 5, 1, 6, 2, 5]))  # Output: 2

print(getMinOperations([2,4,8,16]))  # Output: 4

print(getMinOperations([3,24]))  # Output: 3

print(getMinOperations([1,9,9]))  # Output: 0

print(getMinOperations([1]))  # Output: 0

print(getMinOperations([2]))  # Output: 1

print(getMinOperations([]))  # Output: 0




