inp = int(input('input nums: '))
counts = 0

for i in range(2, (inp // 2) + 1):
    if inp % i == 0:
        counts += 1
        print(i)

print('the number of positive divisors of {} is {}'.format(inp, counts))
