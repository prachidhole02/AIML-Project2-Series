class AdmissionChatbot:
    def __init__(self):
        self.context = {}

    def respond(self, user_input):
        # Define admission-related responses
        responses = {
            "admission_procedure": "To apply for admission, you need to fill out the online application form.",
            "requirements": "Common requirements include high school transcripts, standardized test scores, and letters of recommendation.",
            "deadlines": "The admission deadline for the upcoming semester is March 15th.",
            # Add more responses as needed
        }

        # Check if user input matches any predefined queries
        for query, response in responses.items():
            if query in user_input.lower():
                return response

        # If no predefined response matches, handle accordingly
        return "I'm sorry, I couldn't understand your question. Can you please rephrase it?"

    def chat(self):
        print("Welcome to the College Admission Chatbot! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            response = self.respond(user_input)
            print("Bot:", response)


if __name__ == "__main__":
    bot = AdmissionChatbot()
    bot.chat()
