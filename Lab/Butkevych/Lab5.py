import random


#___task_1__________
random_list = []
for N in range(10):
   random_list.append(int(random.randrange(-50, 50)))
print(random_list)



def max_func(list):
   if max(list) > 0:
      return max(list)
   else: 
      return print("max number < 0 ")


#___task_2__________
str = "dsdsadsadkui12138u(*&*%!@("
def letter_counter(string):
   count = 0
   for char in string:
      if char.isalpha():
         count += 1
   return count

print(letter_counter(str))


#___task_3__________
rand_num = random.randrange(-50, 50)
rand_stepin = random.randrange(-10, 10)

def stepin_func(num, stepin):
   if stepin <= 0:
     return "???"
   else:
      return num**stepin
print("число: ", rand_num, " у степені: ", rand_stepin, " = ", stepin_func(rand_num, rand_stepin))


#___task_4__________
ran_num = random.randrange(1, 20)
def num_counter(n):
   for i in range(1, n):
      print(" ", i)
num_counter(ran_num)


#___task_5__________
rand_height = random.randrange(1, 50)
rand_width = random.randrange(1, 50)

def area_count(height, width):
   if height <= 0 or width <= 0:
     return "???"
   else:
      return height*width;
print("площа прямокутника = ", area_count(rand_height, rand_width))