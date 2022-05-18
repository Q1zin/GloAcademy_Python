n = int(input())

for i in range(n):
    num = int(input())
    if (i == 0):
        max = min = num
    if max < num:
        max = num
        
    if min > num:
        min = num
        
print('Минимум равен', min)
print('Максимум равен', max)
