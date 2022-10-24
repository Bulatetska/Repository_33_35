

      #___task_1_________________                                            
A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
print("елементи A, яких немає в B: ", A - B)


      #___task_2_________________
print("\n")                                                   
print("cпільні елементи А та В: ", A & B)


      #___task_3_________________
print("\n")                                                   
print("об'єднання множин А та В: ", A | B)



      #___task_4_________________
print("\n")                                                   
a = "a14b6fh"
list = []
for i in a:
   list.append(i)
print(set(list))



      #___task_5_________________
print("\n")                                          
a2 = "sakdhsjadkasufdgiulhdiahsdbqiydaiydkasdkancail"
list2 = []
for i2 in a2:
   list2.append(i2)
   
for el in list2:
   if list2.count(el) > 1: 
      print("repeated element: ", el, " number of repetitions: ",list2.count(el))
      for el2 in list2:
         if el2 == el:
            list2.remove(el)         
            
            
   #___task_6_________________         
print("\n")                                               
values = "dsadadhsakndsa" 

keys = []
for k in range(1, len(values)+1):
   keys.append(k)   
   dictionary = dict.fromkeys(keys)
for val in range(len(values)):
   dictionary[keys[val]] = values[val]

for ke, va in dictionary.items():
   if ke % 2 == 0:
      print("key: ", ke, " value:", va)

    
    
    #___task_7_________________
print("\n")                                       
for k_e in dictionary.copy():
   if dictionary[k_e].startswith("a"):
      dictionary.pop(k_e)
print(dictionary)