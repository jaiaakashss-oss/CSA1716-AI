
# Simple Chatbot using NLP

import re
import random

# Chatbot responses
responses = {
    "hello": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you."
    ],
    "how are you": [
        "I am fine. Thank you!",
        "I am doing great!"
    ],
    "your name": [
        "I am a simple NLP chatbot."
    ],
    "help": [
        "Sure! How can I assist you?"
    ],
    "bye": [
        "Goodbye! Have a nice day."
    ],
    "thank you": [
        "You're welcome!",
        "Happy to help!"
    ]
}

# Function to process user input
def chatbot(user_input):

    # Convert text to lowercase
    user_input = user_input.lower()

    # Remove special characters
    user_input = re.sub(r'[^a-z0-9\s]', '', user_input)

    # Tokenization
    words = user_input.split()

    # Match user input with chatbot responses
    for key in responses:

        key_words = key.split()

        if all(word in words for word in key_words):
            return random.choice(responses[key])

    return "Sorry, I don't understand. Can you ask something else?"


# Main program
print("===== SIMPLE NLP CHATBOT =====")
print("Type 'bye' to exit the chatbot.\n")

while True:

    user = input("You: ")

    if user.lower().strip() == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    reply = chatbot(user)

    print("Bot:", reply)
