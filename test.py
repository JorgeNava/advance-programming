nums = [1, 2, 3, 4, 5, 6, 7]
expectedResult = [5, 6, 7, 1, 2, 3, 4]
k = 3

# Get the length of the array
numsLength = len(nums)
# Get the number numbers we should move to the right
# If its bigger than the length of the array then we get its modulo to determine how many
# numbers to move since we had to rotate completly the array (n = 8, k = 15, necesaryMoves = 7)
arrayDivider = k % numsLength
# Create slice of array that will be placed at the begining of the array (sliding them to the right)
firstSlice = nums[numsLength-arrayDivider:]
# Create slice of array that will be placed after the first array (moving them to the right)
lastSlice = nums[:numsLength-arrayDivider]
# Combine both slices of array to create the slided array to the right
nums = firstSlice + lastSlice

print('\n\n\n============================================')
print('Final array: ', nums)
print('Test passed: ', nums == expectedResult)
