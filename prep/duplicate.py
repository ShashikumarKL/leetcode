#contains duplicate

def check_duplicate(nums):
	hash_list = []
	for i in nums:
		if i in hash_list:
			return True
		else:
			hash_list.append(i)
	return False

if __name__ == "__main__":
	nums = [1,2,3,11]
	print(check_duplicate(nums))
