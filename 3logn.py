n=int(input('Введите кол-во чисел в массиве: '))
a=[]
f=1
print()
for i in range (n):
    print('Введите элемент', f ,'массива:')
    a.append(int(input()))
    f+=1
print('Задан массив:')
print(sorted(a)); print()
g=int(input('Введите число для нахождения его в массиве: '))
print()
m = len(b) // 2
l = 0
h = len(b) - 1
q = 0
while b[m] != g and l <= h:
    if g > b[m]:
        l = m + 1
    else:
        h = m - 1
    m = (l + h) // 2
    q += 1
print()
if l > h:
    print('Числа', g ,'нет в массиве')
    print('Количество шагов для нахождния числа', g, ':', q)
else:
    print('Число', g ,'есть в массиве')
    print('Количество шагов для нахождния числа', g, ':', q)
n=int(input('Введите кол-во чисел в массиве: '))
a=[]
f=1
print()
for i in range (n):
    print('Введите элемент', f ,'массива:')
    a.append(int(input()))
    f+=1
print('Задан массив:')
print(sorted(a)); print()
g=int(input('Введите число для нахождения его в массиве: '))
print()
m = len(b) // 2
l = 0
h = len(b) - 1
q = 0
while b[m] != g and l <= h:
    if g > b[m]:
        l = m + 1
    else:
        h = m - 1
    m = (l + h) // 2
    q += 1
print()
if l > h:
    print('Числа', g ,'нет в массиве')
    print('Количество шагов для нахождния числа', g, ':', q)
else:
    print('Число', g ,'есть в массиве')
    print('Количество шагов для нахождния числа', g, ':', q)
n=int(input('Введите кол-во чисел в массиве: '))
a=[]
f=1
print()
for i in range (n):
    print('Введите элемент', f ,'массива:')
    a.append(int(input()))
    f+=1
print('Задан массив:')
print(sorted(a)); print()
g=int(input('Введите число для нахождения его в массиве: '))
print()
m = len(b) // 2
l = 0
h = len(b) - 1
q = 0
while b[m] != g and l <= h:
    if g > b[m]:
        l = m + 1
    else:
        h = m - 1
    m = (l + h) // 2
    q += 1
print()
if l > h:
    print('Числа', g ,'нет в массиве')
    print('Количество шагов для нахождния числа', g, ':', q)
else:
    print('Число', g ,'есть в массиве')
    print('Количество шагов для нахождния числа', g, ':', q)