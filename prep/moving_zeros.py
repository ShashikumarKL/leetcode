def moveZeros(nums):
	for i in nums:
		if i == 0:
			print(nums)
			nums.remove(i)
			nums.append(i)
	return nums

if __name__ == "__main__":
	nums = [ 1, 0,0,0,0, 3, 12, 0]
	result = moveZeros(nums)
	print(result)
