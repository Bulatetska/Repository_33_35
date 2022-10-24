import random
#----key-generator---------------------

textForShifr = open('text.txt', 'r')
fileKey = open('shifrKey.txt', 'w')

text = str(textForShifr.read())

key = []
for i in range(len(text)):
   key.append(random.randrange(1, 10)) 
   
def listToString(list): 
   strKey = ''
   for i in key:
      strKey += str(i)
   return strKey

fileKey.write (listToString(key)) 

shifrKey = open('shifrKey.txt', 'r')
textForShifr = open('text.txt', 'r')
shifredText = open('shifredText.txt', 'w')

#----shifr--------------------------

for i in range (len(text)):
   shifredText.write (chr(ord(text[i]) - int(key[i])))  


#----deshifr------------------------

shifrKey = open('shifrKey.txt', 'r')
shifredText = open('shifredText.txt', 'r')
unShifredText = open('unshifred.txt', 'w')

shText = shifredText.read()

for i in range (len(shText)):
   unShifredText.write (chr(ord(shText[i])+ int(key[i])))


