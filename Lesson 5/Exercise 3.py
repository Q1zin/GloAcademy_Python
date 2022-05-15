num = int(input())

left = num // 1000
right = num % 1000

print()

if (left % 10 + left % 100 // 10 + left // 100) == (right % 10 + right % 100 // 10 + right // 100):
    print('Билет', num, 'счастливый')
else:
    print('Билет', num, 'НЕсчастливый')
