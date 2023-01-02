#Separate the string into groups from 0 to 9 separated by periods, or die trying.

string = '012345678901234567890123456789012345678901234567890123456789'

#eg... ['0123456789', '0123456789']
#return = ['0123456789.0123456789.0123456789.0123456789']

n = 10 #Contain 10 caracteres,then, the range will jump from 0 to 10

comp = [string[i: i + n] for i in range(0, len(string), n)]

retorno = '.'.join(comp)

print(retorno)
