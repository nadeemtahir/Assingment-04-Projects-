import random

JOKES = [
    "Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "What’s a computer’s favorite beatle song? 'Let it B...yte'",
    "Why did the JavaScript developer go broke? Because he kept using 'var' instead of 'let'."
]

PROMPT = "\n🤖 What can I do for you? (Type 'bye' to exit): "
SORRY = "😅 Sorry, I only tell jokes. Try typing something like 'Tell me a joke!'"

def joke_bot():
    print("🤖 Welcome to JokeBot! I'm here to make you laugh.\n")
    
    while True:
        user_input = input(PROMPT).strip().lower()
        
        if user_input == "bye":
            print("👋 Goodbye! Keep smiling 😄")
            break
        
        if "joke" in user_input or "funny" in user_input or "laugh" in user_input:
            print("\n😂 Here's a joke for you:\n")
            print(random.choice(JOKES))
        else:
            print(SORRY)

# Run the bot
joke_bot()
