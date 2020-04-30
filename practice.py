def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        first_num = array[i]
		for j in range(i + 1, len(array)):
		    second_num = array[j]
			if first_num + second_num == targetSum:
			    return [first_num, second_num]
	return []	

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(twoNumberSum([4, 6], 10))
print(twoNumberSum([4, 6, 1], 5))
print(twoNumberSum([4, 6, 1, -3], 3))
print(twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))
print(twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
print(twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))
print(twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163))
print(twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15))
