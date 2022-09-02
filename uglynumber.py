# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

n = 68705

if n == 0:
    print(False)
while n % 2 == 0:
    n = n/2
while n % 3 == 0:
    n = n/3
while n % 5 == 0:
    n = n/5
if n == 1:
    print(True)
print(False)
