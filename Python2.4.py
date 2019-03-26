import random

def func(x):
    if x % 2 == 0:
        return 1
    else:
        return 0


print('Введите N')
n = int(input())
if n <= 10:
    print('N должно быть больше 10!')

list1 = []

for i in range(n):
    element = int(input())
    list1.append(element)
print('----------------------------')
print(list1)
print('----------------------------')
for i in range(5):
    list1.append(random.randint(1, 20))
print(list1)
print('----------------------------')
list2 = filter(func, list1)
list2 = list(list2)
print(list2)

