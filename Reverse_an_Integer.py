number = 123456789
rev = 0

while number:
     tmp = number % 10
     rev = rev * 10 + tmp
     number //= 10

print(rev)


