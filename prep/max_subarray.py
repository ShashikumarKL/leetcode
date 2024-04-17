def maxSubArray(nums):
	maxSub = nums[0]
	curSub = 0
	for n in nums:
		if curSub < 0:
			curSub = 0
		curSub += n
		maxSub = max(maxSub, curSub)
	return maxSub

if __name__ == "__main__":
	print(maxSubArray([-2,1,-3,4,-1,2,1,-5,1]))
