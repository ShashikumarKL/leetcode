def unique_char(text):
	hash_map={}
	for i in text:
		if i not in hash_map:
			hash_map[i]=True
		else:
			hash_map[i]=False
	print(hash_map)
	for index,char in enumerate(text):
		if hash_map[char]:
			return index
	return -1

if __name__ == "__main__":
	print(unique_char("shashikumar"))
