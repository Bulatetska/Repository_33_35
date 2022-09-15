
#___task_1______________

class car:
   def __init__(self, brand, color, engine):
      self.brand = brand
      self.color = color
      self.engine = engine
      
   def goForward(self):
      print(self.color, self.brand, "Going forward!")   
      
   def goBack(self):
      print(self.color, self.brand, "Going back!")

c1 = car("Volkswagen", "white", "1.8")        
print(c1.brand)


#___task_2______________

class car2(car):
   def __init__(self, brand, color, engine):
      super().__init__(brand, color, engine)
      
   def turnLeft(self):
      print(self.color, self.brand, "Turning to the left")
      
   def turnRight(self):
      print(self.color, self.brand, "Turning to the right")

c2 = car2("Opel", "red", "2.2")
print(c2.turnLeft())


#___task_3______________

class plane:
   def __init__(self, model):
      self.model = model
   
   def fly_up(self):
      print("Flying up!")

p1 = plane("Dream")
print(p1.fly_up())


#___task_4______________
#___При успадкуванні класів у нас з`являється доступ до методіс успадкованих класів

class hybrid(car2, plane):
   pass

hybridoid = hybrid("bo", "gray", "5.0")
print(hybridoid.fly_up())   
