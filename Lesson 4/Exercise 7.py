num = int(input())

print('У числa', num, 'сумма последних трех цифр равна', num % 10 + num % 100 // 10 + num % 1000 // 100)
