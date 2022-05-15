num = int(input())

if (num > 36 or num < 0):
    print('ошибка ввода')
elif num == 0:
    print('Зелёный')
elif num < 11:
    if (num % 2 == 0):
        print('Чёрный')
    else:
        print('Красный')
elif num < 18:
    if (num % 2 == 0):
        print('Красный')
    else:
        print('Чёрный')
elif num < 28:
    if (num % 2 == 0):
        print('Чёрный')
    else:
        print('Красный')    
else:
    if (num % 2 == 0):
        print('Красный')
    else:
        print('Чёрный')    
