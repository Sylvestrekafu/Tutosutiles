"""
Les fonctions lambda sont des fonctions anonymes (sans nom) en Python qui peuvent être utilisées
pour créer de petites fonctions simples.
 Elles sont définies à l'aide du mot-clé lambda et peuvent être utilisées dans diverses situations
  où une fonction courte et concrète est nécessaire.

"""
#Calculer le double d'un nombre :
<<<<<<< HEAD
double = lambda x: x * 2
result = double(4)
print(result)  # Affiche : 8

# Additionner deux nombres :
add = lambda a, b: a + b
result = add(3, 5)
print(result)  # Affiche : 8

# Trier une liste de tuples en fonction du second élément :
data = [("pomme", 3), ("banane", 1), ("orange", 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Affiche : [('banane', 1), ('orange', 2), ('pomme', 3)]

# Filtrer les nombres pairs d'une liste :
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Affiche : [2, 4, 6, 8]
=======
# double = lambda x: x * 2
# result = double(4)
# print(result)  # Affiche : 8

# # Additionner deux nombres :
# add = lambda a, b: a + b
# result = add(3, 5)
# print(result)  # Affiche : 8

# # Trier une liste de tuples en fonction du second élément :
# data = [("pomme", 3), ("banane", 1), ("orange", 2)]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)  # Affiche : [('banane', 1), ('orange', 2), ('pomme', 3)]

# # Filtrer les nombres pairs d'une liste :
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Affiche : [2, 4, 6, 8]
>>>>>>> origin/master

# Appliquer une fonction sur chaque élément d'une liste en utilisant map() :
#Application d'une fonction sur chaque élément d'une liste en utilisant la fonction map()

<<<<<<< HEAD
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Affiche [1, 4, 9, 16, 25]

is_palindrome = lambda s: s.lower() == s[::-1].lower()
word = "radar"
result = is_palindrome(word)
print(result)  # Affiche : True
=======
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)  # Affiche [1, 4, 9, 16, 25]

# is_palindrome = lambda s: s.lower() == s[::-1].lower()
# word = "radar"
# result = is_palindrome(word)
# print(result)  # Affiche : True
>>>>>>> origin/master


# Utilisation avec la fonction reduce()
#  nous utiliserons une fonction lambda pour calculer le produit de tous les éléments d'une liste.
from functools import reduce
<<<<<<< HEAD

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print(product)
Affiche : 120

# Création d'une fonction pour additionner deux nombres
def add(x, y):
    return x + y

# Utilisation de la fonction reduce() pour calculer la somme de tous les éléments d'une liste
numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)

# print(result)  # Affiche : 15
=======
#
# numbers = [1, 2, 3, 4, 5]
#
# product = reduce(lambda x, y: x * y, numbers)
#
# print(product)
# Affiche : 120

# Création d'une fonction pour additionner deux nombres
# def add(x, y):
#     return x + y
#
# # Utilisation de la fonction reduce() pour calculer la somme de tous les éléments d'une liste
# numbers = [1, 2, 3, 4, 5]
# result = reduce(add, numbers)
#
# # print(result)  # Affiche : 15
>>>>>>> origin/master
