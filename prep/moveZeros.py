def moveZeros(nums):
	left = 0
	for right in range(len(nums)):
		if nums[right] != 0:
			nums[right], nums[left] = nums[left], nums[right]
			left+=1
	return nums

if __name__ == "__main__":
	nums = [1,0,3,0,12]
	print(moveZeros(nums))
