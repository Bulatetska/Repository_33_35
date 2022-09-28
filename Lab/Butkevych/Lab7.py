import random
import datetime
import json

#___task_1______________________________
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string = ''
for i in range(25):
   string += alphabet[random.randrange(0, 26)];

file = open('random_string.txt', 'w')
file.write(string);


#___task_2______________________________
dictOfGuys = {
   'guys' : [
      {
         'name' : 'Artur',
         'age' : random.randrange(1, 99)  
      }, 
      {
         'name' : 'Keyt',
         'age' : random.randrange(1, 99)  
      },
      {
         'name' : 'Alice',
         'age' : random.randrange(1, 99)  
      },
      {
         'name' : 'Mike',
         'age' : random.randrange(1, 99)  
      }      
   ]
}

currD = datetime.datetime.now().strftime('%d_%m_%Y');
dict = {
   'data' : dictOfGuys,
   'created_at' : currD
}

guys_json = json.dumps(dict, indent=4)

file_json = open('user_data_'+str(currD)+'.json', 'w')
file_json.write(guys_json)