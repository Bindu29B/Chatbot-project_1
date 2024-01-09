import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_TASK = "I can help answer your questions, provide information, and engage in a conversation with you. Feel free to ask me anything!"
R_JOKE = "Sure, here's a joke for you: Why did the computer keep its drink on the windowsill? Because it wanted a cold drink without the Windows!"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response