A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
C = A - B
print("Elements of A that are not in B = ", C)
D = A & B
print("Shared elements of sets = ", D)
E = A | B
print("Union of sets = ", E)

a = 'a14b6f'
chars = list(a)
print(chars)
x = set(chars)
print(x)

L1 = [1, 4, 6, 2, 5, 2, 4, 1, 2, 1, 0, 2]
dc = {} #словник
for i in L1:
    if i in dc:
        dc[i] += 1 #якщо елемент повторюється, то до рахунку повторів +1
    else:
        dc[i] = 1
print("My dictionary: ", dc)
for key, value in dc.items():
    print("The elements {0} appear in L1 : {1}".format(key,value)) #виводить ключ і кількість повторів елемента в списку

word = {1: 'K', 2: 'S', 3: 'D', 4: 'E', 5: 'B', 6: 'C', 7: 'G', 8: 'R', 9: 'I', 10: 'E', 11: 'L', 12: 'T'} #коли виведе парні ключі, то вийде слово
k = word.keys() #витягує всі ключі зі словника word
kk = list(k) #перетворює на список ключів
out = list(filter(lambda x: (x % 2 == 0), kk)) #відсортовує список ключі, залишаючи парні
word2 = {}
for j in out:
    print('(', j, ': ', word[j], ')')
    word2[j] = word[j] #виводить парні ключі і його значення, виходить слово


list_words = {1: 'acrobat', 2: 'sculptor', 3: 'cat', 4: 'apple', 5: 'chair', 6: 'orca', 7: 'doctor', 8: 'aranara', 9: 'octopus', 10: 'water', 11: 'notebook', 12: 'moon'}
w = list(list_words.values()) #список значень словника
#print(w)
w1 = " ".join(w) #перетворення списка на строку
new_word = list(filter(lambda x: x[0] != 'a', w1.split())) #відформатування строки; видалення слів, які починаються з літери 'a' і перетворення на список
#print(new_word)
nlw = {}
for key, value in list_words.items(): #міняє місцями значення  в словнику з ключами
    nlw[value] = key
nlw2 = nlw.keys()
nlw3 = list(nlw2)
for ii in w:
    if ii not in new_word: #якщо значення не в списку, ті слова які починаються з літери "а", то видаляє ключ
        nlw.pop(ii)
#print(nlw)

new_list_words = {} #змінюємо ключі зі значеннями і виводимо результат
for key, value in nlw.items():
    new_list_words[value] = key
print(new_list_words)






