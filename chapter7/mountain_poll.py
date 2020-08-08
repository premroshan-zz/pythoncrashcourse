#to store input in a dictionary

responses = {}

#set a flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input("Enter your name: ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    #find out if anyone else has to answer the poll
    repeat = input("Is someone else using the poll?")
    if repeat == 'no':
        polling_active = False
    
print("Poll Results")
for name, response in responses.items():
    print(f"{name} wants to climb the mountain {response}")