import random

number = 0
cnt = 0
while cnt < 32:
    number = random.randint(0, 15)
    print(number)
    cnt += 1
    if number == 7:
        print('oh-oh')
        break
else:
    print("wow, you're pass")
