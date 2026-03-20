def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("🤖 ChatBot: Hi there! 😊")

        elif "how are you" in user_input:
            print("🤖 ChatBot: I'm just code, but I'm doing great! How about you?")

        elif "your name" in user_input:
            print("🤖 ChatBot: I'm CodeAlpha Bot 🤖")

        elif "help" in user_input:
            print("🤖 ChatBot: I can chat with you! Try saying hello, asking my name, or say bye.")

        elif "bye" in user_input:
            print("🤖 ChatBot: Goodbye! Have a great day! 👋")
            break

        else:
            print("🤖 ChatBot: Hmm... I didn't understand that. Try something else!")

# Run chatbot
chatbot()
