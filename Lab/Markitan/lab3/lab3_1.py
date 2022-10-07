# 1st task:
import random

basic_list = []
for number in range(0, 10):
   basic_list.append(int(random.randrange(1, 999)))
print("list of random 10 numbers: ", basic_list)

list_1 = basic_list
test1 = [list_1.remove(number) if number % 2 == 0 else number for number in list_1]
for number in list_1:
    if number % 2 == 0:
        list_1.remove(number)
    # represents results
    print(number)
