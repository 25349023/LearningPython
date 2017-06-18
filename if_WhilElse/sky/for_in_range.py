name = input('plz input your name: ')
print('len(name) = {}'.format(len(name)))

# 太狂了↓      # zip物件如果拿來用的話, 會變成 tuple物件
for i, c in zip(range((len(name))), name):
    print(i, c)
print()

# 更狂↓        # enumerate物件也是
for i, c in enumerate(name, 1):
    if c.isupper():
        print('\nup!\n')
    print(i, c)
