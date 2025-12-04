string = "Hello"
set_str = set(string)

dict = {}

for element in set_str:
    print(f"{element}:{string.count(element)}")
    dict[element] = string.count(element)

print("Dictionary")
for (key, value) in dict.items():
    print(f'{key}:{value}')

## Existing dic - dict

new_dict = {}
for (key, value) in dict.items():
    new_dict[value] = key

print("Updated dictionary")
for (key, value) in new_dict.items():
    print(f'{key}:{value}')


## Alternate approach 

new_dict2 = {}
for (key, value) in dict.items():
    new_dict2[value] = []


for (key, value) in dict.items():
    new_dict2[value].append(key)

print("Updated dictionary 2")
for (key, value) in new_dict2.items():
    print(f'{key}:{value}')
