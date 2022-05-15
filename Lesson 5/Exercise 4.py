w = int(input())

if (w < 4):
    print('NO')
elif w % 10 % 2 == 0:
    print('YES')
else:
    print('NO')
