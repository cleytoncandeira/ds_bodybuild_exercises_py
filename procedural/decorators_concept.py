"""
Decorators = add, remove, restrict, and modify a def function

What is the problem to be solved?

"""

#Let's say there is a function that reverses strings

#def reverse_string(string):
 #   return string[::-1]

#What happens if this function doesn't deal with a string, but with an int? Gives TypeError
#Soooooooo, how to solved by closure functions?

#Solution by Closure Functions

def create_a_function_(func):
  def inter_to_iterate(*args, **kwargs):   #remember that args and kwargs expands our param numbers; "we don't know what this functions will received!", so, use args and kwargs
      for arg in args:  #now we iterate
          is_string(arg)
      result = func(*args, **kwargs) #after check, we return 
      return result 
  return inter_to_iterate  

@create_a_function_
def reverse_string(string):
    return string[::-1]

def is_string(parameter):
    if not isinstance(parameter, str):
        raise TypeError("This parameter must be a string type!")

#reverse_string_check_it_parameter = create_a_function_(reverse_string) #Instead of using this function coupling, you can simply place the decorator directly in the function.

reverse = reverse_string ("123")        #reverse_string_check_it_parameter('123') < -- how was before

print(reverse)


