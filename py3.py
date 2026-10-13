print("Welcome to the Basic Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hi!")
    elif user == "how are you":
        print("Bot: I'm fine, thanks!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")