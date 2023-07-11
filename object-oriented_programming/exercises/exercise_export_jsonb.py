import json
from exercise_export_jsona import dir_way, Creature, do_dump #import the function what deferring the execution

with open(dir_way, 'r') as file_read:
    data = json.load(file_read)

    c1 = Creature(**data[0])
    c2 = Creature(**data[1])
    c3 = Creature(**data[2])

"""
Interesting comment: when importing the exercise_export_jsona module, 
the json dump method from that module is executed. 
How to make it no longer run? Deferring the execution of your function (json.dump).


in module exercise_export_jsona module it's necessary to put a def function empty

--------------------------

Now, a problem appear. How to execute do_dump just in exercise_export_jsona and not in jsonb? 

__main__ -- first module executable -- this is the solution


"""

