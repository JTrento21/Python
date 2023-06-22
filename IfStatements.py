raining = input("Is it raining? (yes/no)")
ans1 = raining.lower()
if ans1 == "yes":
    windy = input("Is it windy?")
ans2 = windy.lower()
if ans2 == "yes":
    print("It is too windy for an umbrella")
elif ans2 == "no":
    print("Take an umbrella")
elif ans1 == "no":
    print("Enjoy your day!")


print("+---------------------------------------------------------------+")


name = input("What is your name?")

if name == "Joao":
    print("Thats a good name!")
else:
    print("Hello", name)


print("+---------------------------------------------------------------+")