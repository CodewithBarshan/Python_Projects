import nltk
from nltk.chat.util import Chat, reflections
print("Hi,Whats your name?")
def filter_inappropriate(input_text):
    # List of inappropriate words or phrases
    inappropriate_words = ['sex', 'violence', 'drugs', 'weapon', 'kill', 'murder', 'death', 'suicide', 'hate', 'racism', 'curse', 'profanity', 'adult', 'porn', 'nude', 'boobs', 'butt', 'penis', 'vagina', 'xxx']
    # Check if any inappropriate word is in the input
    for word in inappropriate_words:
        if word in input_text.lower():
            return True
    return False

class InappropriateFilterChat(Chat):
    def converse(self, quit="quit"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try:
                user_input = input(">")
            except EOFError:
                print(user_input)
            if filter_inappropriate(user_input):
                print("I'm sorry, I cannot respond to inappropriate content.")
            else:
                response = self.respond(user_input)
                print(response)

pairs = [    ['(my name is)? ?(.*)', ['Hi %2, how can I help you?']],
    ['what|whats is your name?', ['My name is Barshan AI']],
    ['how are you?', ['I am doing well, thank you!']],
    ['(.*) your age?', ['I am an AI language model, so I do not have an age!']],
    ['what can you do?', ['I can answer your questions and chat with you.But right now i am trained on very less data']],
    ['goodbye', ['Goodbye', 'have a great day!']],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
