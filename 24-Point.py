print("Welcome To 24 Points")
point = 0
for a in range(0,10):
    import random
    a1 = random.randint(1, 9)
    a2 = random.randint(1, 9)
    a3 = random.randint(1, 9)
    a4 = random.randint(1, 9)
    print(a1 ," ", a2 ," ", a3 ," ", a4)
    answer = str(input("Answer:"))
    if answer[1] == "+":
        key = int(answer[0]) + int(answer[2])
    elif answer[1] == "-":
        key = int(answer[0]) - int(answer[2])
    elif answer[1] == "*":
        key = int(answer[0]) * int(answer[2])
    elif answer[1] == "/":
        key = int(answer[0]) / int(answer[2])
    elif answer[1] == "^":
        key = int(answer[0]) ** int(answer[2])
    if answer[3] == "+":
        key = key + int(answer[4])
    elif answer[3] == "-":
        key = key - int(answer[4])
    elif answer[3] == "*":
        key = key * int(answer[4])
    elif answer[3] == "/":
        key = key / int(answer[4])
    elif answer[3] == "^":
        key = key ** int(answer[4])
    if answer[5] == "+":
        key = key + int(answer[6])
    elif answer[5] == "-":
        key = key - int(answer[6])
    elif answer[5] == "*":
        key = key * int(answer[6])
    elif answer[5] == "/":
        key = key / int(answer[6])
    elif answer[5] == "^":
        key = key ** int(answer[6])
    if key == 24:
        print("CONGRATULATIONS!")
        point = point + 1
    else:
        print("SORRY U R WRONG!")
print("UR FINAL SCORE:", point)