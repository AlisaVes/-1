x=int(input('Введите количество чисел для сортировки: '))
a=[0]*x
print()
for i in range(x):
    a[i]=int(input('Введите число: '))
print()
print('Метод Sorted: ',sorted(a))
print()
def fun (a):
    for x in range(0,len(a)-1):
        for j in range(0,len(a)-1):
            if (a[j]>a[j+1]):
               a[j],a[j+1]=a[j+1],a[j]
    return a
print('Пузырьковый метод: ',fun(a))