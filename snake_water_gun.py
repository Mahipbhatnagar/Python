
"""
This is the Snake-water-gun game
for a 5 trials.

"""
import random
list = ["Snake", "Water", "Gun"]


c = 0
u = 0
i = 0
while i < 5 :
    a = random.choice(list)
    b = input("\nEnter your choice:\n s-Snake \n w-Water\n g-Gun\n :")
    if a == "Snake" and b == "w":
        print(f"You lose")
        c += 1
        print(f"Result computer {c} user {u}  ")
    elif a == "Snake" and b == "g":
        print(f"You win")
        u += 1
        print(f"Result computer {c} user {u} ")

    elif  a == "Water" and b == "g":
        print(f"You lose")
        c += 1
        print(f"Result computer {c} user {u} ")
    elif a == "Gun" and b == "s":
        print(f"You loss")
        c += 1
        print(f"Result computer {c} user {u} ")

    elif a == "Gun" and b == "w":
        print(f"You win")
        u += 1
        print(f"Result computer {c} user {u} ")
    elif a == "Water" and b == "s":
        print(f"You win")
        u += 1
        print(f"Result computer {c} user {u} ")
    elif a == "Snake" and b=="s":
        print("Both enter the same choice")
        print(f"Result computer {c} user {u} ")
    elif a == "Water" and b=="w":
        print("Both enter the same choice")
        print(f"Result computer {c} user {u} ")
    elif a == "Gun" and b=="g":
        print("Both enter the same choice")
        print(f"Result computer {c} user {u} ")
    else:
        print("You entered wrong value.Restart your game!")
        break
    i = i+1
    print(f"No. of chances left {5-i}")
if u > c:
    print("\n\tYou won the game")
else:
    print("\n\tYou loss the game")