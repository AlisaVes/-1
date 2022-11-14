def dop(n,s,k):
    o = k
    l = (2 * k) + 1
    r = (2 * k) + 2
    if l < s and n[l] > n[o]:
        o = l
    if r < s and n[r] > n[o]:
        o = r
    if o != k:
        n[k], n[o] = n[o],n[k]
        dop(n, s, o)
def ku(n):
    f = len(n)
    for i in range(f,-1,-1):
        dop(n, f, i)
    for i in range(f-1, 0, -1):
        n[i],n[0] = n[0],n[i]
        dop(n, i, 0)
x=int(input('Введите количество чисел для сортировки: '))
a=[0]*x
for i in range(x):
    a[i]=int(input('Введите число: '))
ku(a)
print(a)

def bl(b):
    maxi = max(b)
    s = maxi / len(b)
    bu = []
    for x in range(len(b)):
        bu.append([])
    for i in range(len(b)):
        j = int(b[i] / s)
        if j != len(b):
            bu[j].append(b[i])
        else:
            bu[len(b) - 1].append(b[i])
    for z in range(len(b)):
        f(bu[z])
    fi = []
    for x in range(len(b)):
        fi = fi + bu[x]
    return fi
def f(z):
    for i in range (1, len (z)):
        var = z[i]
        j = i - 1
        while (j >= 0 and var < z[j]):
            z[j + 1] = z[j]
            j = j - 1
        z[j + 1] = var
x = int(input('Введите количество чисел в массиве: '))
b = [0] * x
for i in range(x):
    b[i] = int(input('Введите элемент массива:'))
res = bl(b)
print(res)