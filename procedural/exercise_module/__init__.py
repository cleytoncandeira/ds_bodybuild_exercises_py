# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy
from source import produtos

new_products = [ {**p, 'preco': round(p['preco'] * 1.1, 2)}
                for p in copy.deepcopy(produtos)]


print(*produtos, sep = '/n')
print()
print(*new_products, sep='/n')

    
decrescent_products_by_name = sorted(copy.deepcopy(new_products), 
                                    key = lambda y: y['nome'], 
                                    reverse = True )

ascendent_products_by_precos = sorted(copy.deepcopy(new_products),
                                        key = lambda y: y['preco'])

print(*decrescent_products_by_name, sep = '/n')
print()
print(*ascendent_products_by_precos, sep = '/n')


    
