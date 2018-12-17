import random
print ("""Welcome!
Let's plat a game. I will think of a number and you have to guess it.""")
print ("""Menu:
1. Start
2. Quit
""")
x = int(input())
while x==1:
    answer = random.randint(0,100)
    print("I have thought of a number. Start Guessing.")
    guess = int(input("Guess: "))
    while guess!=answer:
        if guess>=answer*2:
            print("It's too high!")
        elif guess>answer:
            print("It's high but close.")
        elif guess<=answer/2:
            print("It's too low!")
        elif guess<answer:
            print("It's low but close.")
        else:
            print("You are guessing a number, right?")
        guess = int(input("Guess Again: "))

    print("Cheer! %d is the number." % answer)
    print ("""Menu:
    1. Play Again
    2. Quit
    """)
    x= int(input())

print("Good Bye!")
