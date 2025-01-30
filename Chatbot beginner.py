# Import the random module to add some variety to our responses
import random

# Define a dictionary of questions and possible answers
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Greetings!"],
    "how are you": ["I'm doing well, thanks!", "I'm fine, how about you?", "All good here!"],
    "what's your name": ["My name is ChatBot.", "I'm ChatBot, nice to meet you!"],
    "bye": ["Goodbye!", "See you later!", "Bye bye!"],
}

# Function to get a response from the chatbot
def get_response(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Check if the user input matches any of our predefined questions
    for question, answer_list in responses.items():
        if question in user_input:
            # If there's a match, return a random response from the answer list
            return random.choice(answer_list)
    
    # If no match is found, return a default response
    return "I'm not sure how to respond to that. Can you try asking something else?"

# Main chat loop
print("ChatBot: Hello! I'm a simple chatbot. You can say 'bye' to exit.")
while True:
    # Get user input
    user_input = input("You: ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'bye':
        print("ChatBot: Goodbye! It was nice chatting with you.")
        break
    
    # Get and print the chatbot's response
    response = get_response(user_input)
    print("ChatBot:", response)