number = int(input("Plz Guess An Integer:"))
import random
answer = random.randint(0,100)
s = 0
while s == 0:
    if number < answer:
        print("TOO SMALL!")
        number = int(input("Plz Guess An Integer:"))
    elif number > answer:
        print("TOO BIG!")
        number = int(input("Plz Guess An Integer:"))
    else:
        print("U R RIGHT!")
        s = s + 1