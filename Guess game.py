n = 18
print("You have 9 guess")
i = 9
while(1):
    if i>0:
        a = int(input("Guess the no.:"))
        if a > n:
            print("The no. is smaller than", a)
        elif a < n:
            print("The no. is greater than", a)
        else:
            print("you won the game")
            break
        print("The no. of guesses left",i-1)


    else:
        print("Game is end you have 0 guess is left")
        break

    i=i-1
