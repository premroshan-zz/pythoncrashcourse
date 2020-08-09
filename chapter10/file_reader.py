with open('/Users/premroshannair/development/pythoncrashcourse/chapter10/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

filename = '/Users/premroshannair/development/pythoncrashcourse/chapter10/pi_digits.txt'

lines = []
with open(filename) as fobject:
    lines = fobject.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

