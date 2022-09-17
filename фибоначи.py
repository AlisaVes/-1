x = int(input())
a = [1, 1]
while x >= a[-1] + a[-2]:
    if x == a[-1] + a[-2]:
        print('fib')
    a.append(a[-1]+a[-2])

for i in range (2, x):
    if x % i == 0:
        print('false')
    else:
        print('true')
