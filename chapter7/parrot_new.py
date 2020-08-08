prompt = "Tell me something and i will repeat it back to you"
prompt += "\nPress escape to quit: "
message = ''

while message != 'quit':
    message = input(prompt)
    print(message)
