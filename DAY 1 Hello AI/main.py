print("HEllo! I am Ai Bot. What's your name?")

name = input()

print(f"Nice to meet you,{name} ")

print("How are you  feeling today? (good/bad)")
mood = input().lower()

if mood == "good":
 print("I am glad to hear that!")
elif mood == "bad":
  print("I amm sorry to hear that. Hope things het better better soon.")
else:
  print("I see. Sometimes it's hard to put feelings into words.")

print(f"It was nice chatting with you {name}. Goodbye!")
