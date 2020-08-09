from survey import AnonymousSurvey

# Define a question and make a survey
question= "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and record responses
my_survey.show_question()

print("Enter q at any time to quit:")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print(f"The survey responses are {my_survey.show_results()}")
