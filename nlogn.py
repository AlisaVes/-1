def m(l, r):
    res = []
    i = j = 0
    llen, rlen = len(l), len(r)
    for K in range(llen + rlen):
        if i < llen and j < rlen:
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        elif i == llen:
            res.append(r[j])
            j += 1
        elif j == rlen:
            res.append(l[i])
            i += 1
    return res
def ms(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    l = ms(nums[:mid])
    r = ms(nums[mid:])
    return m(l, r)
n=int(input('Введите кол-во чисел в массиве: '))
a=[]
f=1
print()
for i in range (n):
    print('Введите элемент', f ,'массива:')
    a.append(int(input()))
    f+=1
print(ms(a))