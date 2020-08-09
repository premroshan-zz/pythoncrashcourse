print("Give me two numbers to divide")
print('Enter q to quit')

while True:
    first_number = input('\nEnter the first number:')
    if first_number == 'q':
        break
    second_number = input('\nEnter the second number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cant divide by 0, please try again')
    else:
        print(answer)