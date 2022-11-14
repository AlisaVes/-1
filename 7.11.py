import modr
import timeit

x=int(input('Введите количество чисел для сортировки: '))
a=[0]*x
for i in range(x):
    a[i]=int(input('Введите число: '))
n = input('Для сортировки методом "быстрая сортировка", нажмите 1. Для сортировки методом "рассческа", нажмите 2: ')
if n == 1:
    print(modr.sr(a))
    print(timeit.timeit(setup=set_up, number=100000, globals=globals()))
else:
    print(modr.rs(a))
    print(timeit.timeit(setup=set_up, number=100000, globals=globals()))