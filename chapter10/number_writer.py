import json

numbers = [2,3,5,6,11,13]

filename = 'numbers.json'

with open(filename,'w') as f:
    json.dump(numbers,f)

print(numbers)