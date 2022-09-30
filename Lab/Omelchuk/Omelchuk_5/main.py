list1 = [5, 2, 7, 0, 1, 9, 15, 11, 4]
max1 = max(list1)
list2 = [-5, -2, -7, -1, -9, -15, -11, -4]
max2 = max(list2)

def MaxList(mx):
    if mx < 0:
        print("Number is less than 0")
        return None
    else:
        return mx

print(MaxList(max1)) #task 1
MaxList(max2)


word = "brain" #5
def Word(w):
    l = len(w)
    return l

print(Word(word)) #task 2


def Power_Number(num, pow):
    if pow >= 0:
        x = num**pow
        return x
    else:
        print("Power of number is negative")
        return None

print(Power_Number(2, 4)) #task 3
Power_Number(3, -3)


def Natural(n):
    A = []
    i = 1
    while i <= n:
        A = A + [i]
        i = i + 1
    return A

print(Natural(6)) #task 4

def Area(a, b):
    if a > 0 and b > 0:
        return a * b

print (Area(7, 5)) #task 5