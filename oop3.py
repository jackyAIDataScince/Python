class Pet:
     def __init__(self, name, age):
        self.name = name
        self.age  = age
        
     def show(self):
		print("I am years old") 
		
     def speak(self):   
        print("Speak ")
        
class Cat(Pet):
    def __init__(self, name, age , color):	 
		self.color = color
		Pet.__init__(self,name,age)
            
    
    def show(self):
		print("I am years old") 
                
    def speak(self):
		 print("Meow")    

class Dog(Pet):    
     def speak(self): 
		 print("Bark")

p = Pet("Kittie",23)
p.show()
p.speak()

d = Dog("Gigi",22)
d.speak()

c = Cat("Cat",22,"Red")
c.show()

