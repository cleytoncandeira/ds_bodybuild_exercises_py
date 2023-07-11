#first classe

class Person:
    def __init__(self, name, surname): #can received parameters - args
        self.name = name
        self.surname = surname
    def walking(self):
        print(f'{self.name} is walking in the park')    

p1 = Person('Cleyton', 'Candeira') #creates the person instance and consequently creates Person 1

#p1.name = 'Cleyton' #attributes are the values inside the object
#p1.surname = 'Candeira'

print(p1.name, p1.surname)

#methods are the functions inside the class;
#when a functions is inside the class, its name is "method"

#__init__ method initializing the attributes in the class
#are one of the executable things

#how to execute certain action in class? use method! 

#callable a method walking

p1.walking() #if you print the method, its return None







