#motorcycles.py

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles_new = []
motorcycles_new.append('bajaj')
motorcycles_new.append('honda')

print(motorcycles_new)

motorcycles_new.insert(0,"prem")
print(motorcycles_new)

del motorcycles_new[0]
print(motorcycles_new)

popped_motorcycle = motorcycles_new.pop()
print(popped_motorcycle)

print(popped_motorcycle)

