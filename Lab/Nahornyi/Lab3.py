import random

li = []
l_size = int(input("Розмір списку: "))

for i in range(0, l_size):
    li.append(int(random.randrange(1, 100)))
print("Вхідний список: ", li)

dli = []
for el in li:
    if el % 2 == 0:
        dli.append(el)
fli = []

for x in li:
    if x not in dli:
        fli.append(x)
print("Видалені парні номери: ", fli)

for y in range(0, len(fli)):
    fli[y] **= 2
print("В квадраті: ", fli)

maxi = fli[0]
for d in fli:
    if maxi < d:
        maxi = d
print("Максимальне число: ", maxi)
