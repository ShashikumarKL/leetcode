def two_sum(numbers, target):
	indexMap = {}
	for i,n in enumerate(numbers):
		diff = target - n
		if diff in indexMap:
			return([indexMap[diff],i])
		indexMap[n]=i
		

if __name__ == "__main__":
	numbers = [2,1,3,5,45,23,12,23,4,5,67,8]
	target = 11
	print(two_sum(numbers, target))
