# Ne modifiez que les lignes commençant par ICI

# Créez une variable nommée number et assignez-lui la valeur 10
from __future__ import division


number=10
print("number vaut", number)
# Décrémentez sa valeur par 2
number-=2
print("Apres decrementation, number vaut", number)

# Créez une autre variable nommée square valant le carré de number
square=number**2
print("square vaut", square)

# Créez une dernière variable nommée root valant la racine carrée de number
root=number**0.5
print("root vaut", root)

# Faites une division entière de root par 2 et affichez le résultat
division=root//2
print("division vaut",division)
