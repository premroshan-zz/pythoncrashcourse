class AnonymousSurvey:
    """Collect anonymous answers to a survey question"""

    def __init__(self,question):
        """Store a question and prepare to store responses"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Print the question"""
        print(self.question)

    def store_response(self,response):
        """Add the response to set of responses"""
        self.responses.append(response)

    def show_results(self):
        print("Survey Results")
        for response in self.responses:
            print(f"-{response}")
            