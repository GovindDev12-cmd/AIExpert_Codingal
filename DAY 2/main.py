import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.RED}Hello World!{Style.RESET_ALL}")
user_name = input(f"{Fore.GREEN}Welcome to the Sentiment Spy: {Style.RESET_ALL}")
if not user_name:
    user_name = "Mysterious Stranger"

conversation_history = []

print(f"{Fore.MAGENTA} Hello {user_name}, I am your AI assistant. How can I help you today?")
print(f"Type a sentece to analyze its sentence.")
print(f"Type {Fore.YELLOW}'reset'{Fore.MAGENTA}'hsitory'{Fore.YELLOW}'exit' {Fore.MAGENTA} to perform respective action ")
while True:
    user_input = input(f"{Fore.GREEN} {user_name}: ").strip()
    if not user_input:
        print(f"{Fore.RED} Please enter a valid senetnce.")
        continue
    elif user_input.lower() == "exit":
        print(f"{Fore.MAGENTA} Goodbye {user_name}!")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.MAGENTA} Conversation history has been reset.")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW} No conversation history avaiable.")
            continue

    else:
        print(f"{Fore.CYAN} No converation History avaible.")
        for idx, (text, sentiment) in enumerate(conversation_history, start=1)
          print(f"{Fore.YELLOW} {idx}. {Fore.WHITE}Text: {text}")
          print(f"Sentiement: {sentiment}")
        print(f"{Fore.CYAN}")
    continue

blob = TextBlob(user_input)
ploarity = blob.sentiment.polarity
if ploarity > "0":
    sentiment = "Postive"
    color = Fore.GREEN
elif ploarity < 0:
    sentiment = "Negative"
    color = Fore.RED
else:
    sentiment = "Netural"
    color = Fore.BLUE
print(f"{color} sentiment: {sentiment}")
conversation_history.append((user_input, sentiment))
