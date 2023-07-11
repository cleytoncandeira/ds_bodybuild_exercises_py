"""
Create a duplicate, triple, quadruple, quintuple and so on a number

"""

#what is the def classic view problem?

def duplicate(number):
    return number * 2

def triple(number):
    return number * 3

def quadruple(number):
    return number * 4

#How long will you create def functions? 

#solution:

def multiple(multiply_number): #how many times do you want to multiply this number?
    def multiply(number):
        return multiply_number * number
    return multiply

#test our closure solution

duplicate = multiple(2)
print(duplicate(6))
