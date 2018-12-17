import random
print("Welcome! This is Dice Rolling Simulator")
print("""Menu:
1 = Start
2 = Quit""")
x = int(input())
while x==1:
    print (random.randint(1,6))
    print ("""Menu:
    1 = Roll Again
    2 = Quit""")
    x=int(input())

print ("Good Bye!")
