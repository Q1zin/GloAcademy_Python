n = int(input())

count = 0

for i in range(n):
    num = int(input())
    if num % 2 == 1:
        count += 1
        
if count == n:
    print('YES')
else:
    print('NO')
