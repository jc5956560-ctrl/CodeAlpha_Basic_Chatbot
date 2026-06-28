def chatbot():

    print("welcome to basic chatbot!")
    print("typ bye to exit.")

    while True:

        user = input("you:")
        if user == "hello":
            print("Bot.hi!")
        elif user == "how are you":
                print("Bot.i am fine, thanks!")
        elif user == "bye":
                    print("Bot: goodbye!")
                    break
        else:
            print("Bot:sorry,i don't understand.")
chatbot()