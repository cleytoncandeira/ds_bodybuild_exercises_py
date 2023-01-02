'''
Create a function that finds the first duplicate number from the following deadly list. 
Note: the number is only considered duplicated from its second occurrence on. 
If no duplicate number is found, return -1.

list_of_list_of_integers = [
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
                            [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
                            [3, 8, 2, 8, 6, 7, 7, 3, 1, 9], 
                            [4, 8, 8, 8, 5, 1, 10, 3, 1, 7], 
                            [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
                            [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
                            [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
                            [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
                            [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
                            [5, 3, 1, 8, 5, 7, 1, 8, 8, 7], 
                            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
                            ]
'''
list_of_list_of_integers = [
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
                            [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
                            [3, 8, 2, 8, 6, 7, 7, 3, 1, 9], 
                            [4, 8, 8, 8, 5, 1, 10, 3, 1, 7], 
                            [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
                            [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
                            [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
                            [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
                            [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
                            [5, 3, 1, 8, 5, 7, 1, 8, 8, 7], 
                            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
                            ]


'''
Show your best!

'''

def duplicates(parameter):
    repeated_values = -1
    values = set()
  
    for h in parameter:
        if h in values:
            repeated_values = h
            break      #At the first duplicated value the "for" repeat stops

        values.add(h)

    return repeated_values

#What if the function doesn't find any duplicate values? It returns -1

for i in list_of_list_of_integers: #These are the key figures for each list
    print(i, duplicates(i))