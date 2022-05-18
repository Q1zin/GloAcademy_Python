n = int(input())

flag = 0

for i in range(n):
    num = int(input())
    if num % 2 == 1:
        flag = 1
        
if flag:
    print('YES')
else:
    print('NO')
