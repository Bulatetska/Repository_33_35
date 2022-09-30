import random
import string
import json
import pickle
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

name_list = ["Arthur", "Kate", "Alice", "Mike"]
age_list = random.sample(range(1,101),4)


i = 0
list_dict = []

while i < 4:
    list_dict.append(dict([(name_list[i], age_list[i])]))
    i = i + 1

#3print(list_dict)
date_list = ["25.01.2003", "04.11.1999", "20.07.2000", "14.03.2004"]

dict_date = dict(zip(date_list, list_dict))
print(dict_date)

date = list(dict_date.keys())
key = input()
P = []
for s in date:
    if s==key:
        P=P+[i]
    i=i+1

if len(P)>0:
    current_date = key

else:
    current_date = "no date"

f1 = open('random_string.txt','wt')
f1.write("Random string: ")
f1.write(get_random_string(25))
f1.close()

#f2 = open(f"{current_date}.json", 'wb')
f2 = open(f"{current_date}.json", 'w')
f2.write(json.dumps(dict_date))
f2.close()