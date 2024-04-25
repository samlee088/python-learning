class AnonymousSurvey:
    """Collect anonymous answers to a survey question"""

    def __init__(self, question):
        """Store a question and prepare to store answers"""
        self.question=question
        self.answers = []

    def show_question(self):
        """Show the survey questions"""
        print(f"{self.question}")

    def store_response(self, answer):
        """Store an answer to a response"""
        self.answers.append(answer)

    def show_results(self):
        """Show all of the responses that have been given"""
        print("Survey Results")
        for response in self.answers:
            print(f"-{response}")

    