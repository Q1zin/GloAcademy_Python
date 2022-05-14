num_1 = int(input())

first = num_1 // 100
thirt = num_1 % 10
second = num_1 // 10 % 10
print('Сумма цифр числа', num_1, 'равна', first + second + thirt)
print('Произведение цифр числа', num_1, 'равна', first * second * thirt)
