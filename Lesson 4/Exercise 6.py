num = int(input())

print(max(num % 10, num % 100 // 10, num // 100 % 10, num // 1000))
