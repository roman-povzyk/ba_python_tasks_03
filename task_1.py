word = input('Введіть слово: ')

if len(word) < 2:
    print()
else:
    print(word[:2] + word[-2:])
