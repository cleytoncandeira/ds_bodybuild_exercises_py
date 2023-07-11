'''
Exercise - save your class in a JSON file; 
Save your class data in JSON; 
and then create the class instances with the saved data again.

Do it in separate files.

'''
import json


class Creature:
    def __init__(self, kingdom, phylum, clas, order, night = False):
        self.kingdom = kingdom
        self.phylum = phylum
        self.clas = clas
        self.order = order
    
    def hunting(self):
        night = True
        if self.order == 'strigiformes' or self.order == 'rodentia':
            return print(f'Maybe we creature is hunting at night')
       
        print('Maybe we creature is sleeping')
    
    def export_json(self):
        return Creature.__dict__
        
c1 = Creature('animalia', 'chordata', 'aves', 'strigiformes')
c2 = Creature('animalia', 'chordata', 'mammalia', 'rodentia')
c3 = Creature('animalia', 'chordata', 'mammalia', 'carnivora')


#c1.hunting()
#c2.hunting()
#c3.hunting()

#print(c1.__dict__)

json_file = [vars(c1), c2.__dict__, vars(c3)] #transform this object class in some serializable

dir_way = 'object-oriented_programming/exercises/json_file_exercise.json'

def do_dump(): #see last comment in exercise_export_jsonb
    with open (dir_way, 'w') as file:
        json.dump(json_file, file, ensure_ascii = False, indent = 2) #now json.dumb can read it

if __name__ == '__main__':
    do_dump()