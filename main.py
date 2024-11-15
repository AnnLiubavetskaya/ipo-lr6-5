import random

pozitive = 0
negative = 0
neitral = 0

poz_list = []
neg_list = []
neit_list = []

list = [random.randint(-50,50) for a in range(25)]

for i in list :
    if i > 0:
        pozitive += 1
        poz_list.append(i)
    if i < 0:
        negative += 1
        neg_list.append(i)
    if i == 0:
        neitral += 1
        neit_list.append(i)

if pozitive > 0 :
    procent_poz = (pozitive / 25) * 100
else:
    procent_poz = 0

if negative > 0 :
    procent_neg = (negative / 25) * 100
else:
    procent_neg = 0

if neitral > 0 :
    neit_proc = (pozitive / 25) * 100
else:
    neit_proc = 0

min = min(list)
max = max(list)

#Результаты:

print("Ваш список из случайных целых чисел от -50 до 50 из 25 элементов.", list)
print("Количество положительных числел в списке: ", pozitive)
print("Количество отрицательных числел в списке: ", negative )
print("Количество нулей в списке: ", neitral)
print("Положительные числа из списка: ", poz_list)
print("Отрицательные числа из списка: ", neg_list )
print("Положительные числа из списка: ", neit_list)
print("Процент положительных чисел списка: ", procent_poz)
print("Процент отрицательных чисел списка: ", procent_neg)
print("Процент нулей в списке: ", neit_proc)
print("Минимальное число списка: ", min)
print("Минимальное число списка: ", max)


 

