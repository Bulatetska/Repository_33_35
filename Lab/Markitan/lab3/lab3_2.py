# 2nd task:
import random

basic_list = []
for i in range(0, 10):
   basic_list.append(int(random.randrange(1, 999)))
print("list of random 10 numbers: ", basic_list)

basic_list = [number**2 for number in basic_list]
# represents results
for number in basic_list:
    print(number)