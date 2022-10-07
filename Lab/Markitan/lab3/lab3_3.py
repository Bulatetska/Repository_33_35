# 3rd task:
import random

basic_list = []
for i in range(0, 10):
   basic_list.append(int(random.randrange(1, 999)))
print("list of random 10 numbers: ", basic_list)

# represents results
print('the max:' + str(max(basic_list)))
