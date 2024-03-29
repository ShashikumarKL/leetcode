dict1 = {"value": "11"}

dict2 = dict1.copy()
print(dict1)
print(dict2)


print(id(dict1))
print(id(dict2))

dict2["value"] = 22

print(dict1)
print(dict2)

print(id(dict1))
print(id(dict2))