#Method and class method aplications

"""
In this example, the Connection class create a network class, 
That received a "none" value name and password.

We wanna modify the 'self.name = None' to receive a value = 'Name"

How we do it? 

First, create a 'setter' - setter is a def function that receive a parameter 
and input this value in a attribute - 


"""
class Connection:
    def __init__(self, host = 'localhost'):
        self.host = 'host'
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password): #an instance method that modify another instance method
        self.password = password 

    
