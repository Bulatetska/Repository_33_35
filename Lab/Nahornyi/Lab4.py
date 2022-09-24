A = [3, 5, 11, 7, 4, -3]
B = [11, 5, 8, 1, 10, 7]

res = [x for x in A if x not in B]

res1 = [x for x in A if x in B]
print ("Є в А, немає в В", res)
print ("Спільні елементи", res1)
print ("Об'єднані: ", A + B)
