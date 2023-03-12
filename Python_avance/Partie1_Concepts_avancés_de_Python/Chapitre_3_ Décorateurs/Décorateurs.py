"""
Les décorateurs sont une fonctionnalité avancée de Python qui permettent de modifier
le comportement d'une fonction ou d'une classe sans modifier son code source.
 Les décorateurs sont utilisés pour ajouter des fonctionnalités telles que la mise en cache, la vérification des entrées, la journalisation, etc.

Dans ce chapitre, nous commençons par expliquer le fonctionnement des décorateurs en Python.
 Nous montrons comment les décorateurs peuvent être utilisés pour ajouter du code avant et après l'exécution d'une fonction, ou pour modifier le comportement d'une fonction en temps réel.

Nous abordons également la création de ses propres décorateurs, qui permet de créer des décorateurs personnalisés pour répondre aux besoins
spécifiques d'une application. Nous montrons comment créer une fonction qui prend une fonction en argument et renvoie une nouvelle
fonction décorée avec des fonctionnalités supplémentaires.

Enfin, nous explorons les avantages de l'utilisation des décorateurs en matière de modularité, de réutilisabilité et de maintenabilité du code. Nous montrons comment les décorateurs peuvent être utilisés pour ajouter des fonctionnalités génériques à plusieurs fonctions ou classes, sans avoir à les répéter plusieurs fois.
"""

# Fonctionnement des décorateurs

"""
Les décorateurs sont des fonctions qui prennent une autre fonction en argument, la modifient d'une manière ou d'une autre, 
puis la renvoient. En Python, les décorateurs sont définis en utilisant le symbole "@", 
suivi du nom du décorateur. Voici un exemple de décorateur qui ajoute une fonctionnalité de mise en cache à une fonction :
"""

def memoize(func):
    cache = {}

    def wrapped(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapped

@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

"""
Dans cet exemple, le décorateur "memoize" prend une fonction "func" en argument et renvoie une nouvelle fonction 
"wrapped" qui utilise un dictionnaire "cache" pour stocker les résultats précédents de la fonction. 
Si les arguments sont déjà dans le cache, la fonction renvoie directement la valeur stockée, 
sinon elle appelle la fonction originale et stocke le résultat dans le cache.

Le décorateur est appliqué à la fonction "fibonacci" en utilisant l'annotation "@memoize". 
Cela a pour effet de remplacer la fonction originale par la fonction décorée, qui ajoute automatiquement la mise en cache.
"""

# Création de ses propres décorateurs

# Pour créer un décorateur personnalisé, il suffit de définir une fonction qui prend une fonction en argument et renvoie une nouvelle fonction modifiée. On peut ensuite utiliser cette fonction comme décorateur en l'appliquant à une autre fonction à l'aide de l'annotation "@".
# Voici un exemple de décorateur personna=isé qui mesure le temps d'exécution d'une fonction :


import time

def measure_time(func):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("La fonction", func.__name__, "a pris", end_time - start_time, "secondes.")
        return result

    return wrapped


# Chapitre 3 : Décorateurs


"""
Les décorateurs sont des fonctions qui permettent de modifier le comportement d'une autre fonction sans la modifier directement. Ils sont un outil puissant pour la programmation fonctionnelle en Python, et sont largement utilisés pour des tâches telles que la gestion de la mémoire cache, la journalisation, la mesure du temps d'exécution, etc.

Dans ce chapitre, nous expliquons le fonctionnement des décorateurs en Python, en montrant comment les créer et comment les utiliser pour modifier le comportement des fonctions. Nous abordons également les décorateurs de classe, qui permettent de modifier le comportement d'une classe entière.

Enfin, nous explorons les avantages des décorateurs en matière de modularité, de réutilisabilité et de maintenabilité du code. Nous montrons comment les décorateurs peuvent être utilisés pour créer des programmes plus élégants, plus flexibles et plus faciles à maintenir.

"""

# Fonctionnement des décorateurs

"""
En Python, les décorateurs sont des fonctions qui prennent une autre fonction comme argument, et renvoient une fonction modifiée. Les décorateurs sont appliqués en utilisant la syntaxe "@decorator" au-dessus de la fonction à décorer. """


def memoize(func):
    cache = {}

    def wrapped(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapped

@memoize
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



"""

Dans cet exemple, le décorateur "memoize" prend une fonction "func" comme argument, et renvoie une fonction "wrapped" qui ajoute une mémoire cache à la fonction d'origine. La fonction "wrapped" vérifie d'abord si les arguments ont déjà été calculés et stockés dans la mémoire cache, et renvoie le résultat stocké le cas échéant. Sinon, la fonction d'origine est appelée pour calculer le résultat, qui est ensuite stocké dans la mémoire cache et renvoyé.

Le décorateur est appliqué à la fonction "fibonacci" en utilisant la syntaxe "@memoize". Cela signifie que la fonction "fibonacci" sera remplacée par la fonction "wrapped" modifiée par le décorateur. """

# Décorateurs de classe

"""
Les décorateurs de classe sont similaires aux décorateurs de fonction, mais sont appliqués à une classe entière au lieu d'une fonction individuelle. Ils sont souvent utilisés pour ajouter des fonctionnalités globales à une classe, comme la journalisation, la mesure du temps d'exécution, etc.

Voici un exemple de décorateur de classe qui ajoute une fonction de journalisation à une classe "Personne" :

"""

def loggable(cls):
    def wrapped(*args, **kwargs):
        result = cls(*args, **kwargs)
        print("Objet créé :", result)
        return result

    return wrapped

@loggable
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


# Dans cet exemple, le décorateur de classe "loggable" prend une classe "cls" comme argument, et renvoie une fonction "wrapped" qui ajoute



# Chapitre 3 : Décorateurs

"""

Les décorateurs sont des fonctions qui prennent une autre fonction en argument et retournent une fonction modifiée. Les décorateurs sont un outil puissant de Python qui permet de modifier le comportement des fonctions sans les modifier directement. Les décorateurs peuvent être utilisés pour ajouter des fonctionnalités à une fonction, pour surveiller son exécution, pour limiter l'accès à une fonction, pour la mettre en cache, etc.

Dans ce chapitre, nous commençons par expliquer le fonctionnement des décorateurs en Python. Nous montrons comment créer un décorateur simple qui ajoute un message d'entrée et de sortie à une fonction.

Nous abordons ensuite la création de décorateurs plus avancés, qui permettent de modifier le comportement de la fonction en fonction de son contexte d'utilisation. Nous montrons comment utiliser des décorateurs de classe pour ajouter des fonctionnalités à une classe, comment utiliser des décorateurs avec des arguments, et comment chaîner des décorateurs pour obtenir des effets complexes.

Enfin, nous explorons les avantages des décorateurs en matière de modularité, de réutilisabilité et de lisibilité du code. Nous montrons comment les décorateurs peuvent être utilisés pour ajouter des fonctionnalités sans alourdir le code, pour séparer les préoccupations dans le code, et pour rendre le code plus facile à comprendre et à maintenir.

"""

# Fonctionnement des décorateurs

"""

Le fonctionnement des décorateurs est basé sur la notion de fonction comme objet de première classe en Python. Cela signifie que les fonctions peuvent être passées en argument à d'autres fonctions, et qu'elles peuvent être retournées par d'autres fonctions. Les décorateurs utilisent cette propriété pour modifier le comportement d'une fonction en l'entourant d'une autre fonction.

Voici un exemple de décorateur simple qui ajoute un message d'entrée et de sortie à une fonction :

"""

def trace(func):
    def wrapper(*args, **kwargs):
        print("Entrée :", args, kwargs)
        result = func(*args, **kwargs)
        print("Sortie :", result)
        return result
    return wrapper

@trace
def say_hello(name):
    return "Bonjour, " + name + " !"

print(say_hello("Alice"))


"""

Dans cet exemple, le décorateur "trace" prend une fonction en argument ("func"), et retourne une nouvelle fonction ("wrapper") qui entoure la fonction initiale. La fonction "wrapper" affiche un message d'entrée avant d'appeler la fonction initiale, puis affiche un message de sortie après avoir récupéré le résultat de la fonction initiale.

Le symbole "@" est une syntaxe raccourcie qui permet d'appliquer un décorateur à une fonction. Dans l'exemple ci-dessus, la fonction "say_hello" est décorée avec le décorateur "trace", ce qui ajoute le comportement de traçage à la fonction.

"""

# Décorateurs de classe et décorateurs avec des arguments

"""
Les décorateurs peuvent également être utilisés avec des classes et avec des arguments. Voici un exemple de décorateur de classe qui ajoute une méthode "double" à une classe :

"""

def add_double(cls):
    def double(self):
        return self * 2
    cls.double = double
    return cls

@add_double
class MyInt(int):
    pass

x = MyInt(5)
print(x.double())



# Chapitre 3 : Décorateurs

"""

Les décorateurs sont une fonctionnalité avancée de Python qui permettent de modifier le comportement des fonctions et des classes sans les modifier directement. Les décorateurs sont des fonctions qui prennent une autre fonction ou une classe comme argument, et qui renvoient une nouvelle fonction ou une nouvelle classe qui a un comportement modifié.

Dans ce chapitre, nous commençons par expliquer le fonctionnement des décorateurs, en montrant comment créer et utiliser des décorateurs simples. Nous abordons ensuite des concepts plus avancés, tels que les décorateurs imbriqués, les décorateurs de classe et les décorateurs de méthode.

Nous explorons également des cas d'utilisation pratiques des décorateurs, tels que la mesure du temps d'exécution des fonctions, la vérification des types d'arguments, la gestion des erreurs et des exceptions, etc.

Enfin, nous montrons comment les décorateurs peuvent améliorer la lisibilité, la modularité et la réutilisabilité du code, en permettant de factoriser des comportements communs et de séparer les préoccupations.

"""

# Fonctionnement des décorateurs

"""
Un décorateur est une fonction qui prend une autre fonction comme argument, et qui renvoie une nouvelle fonction qui a un comportement modifié. Voici un exemple simple :

"""

def my_decorator(func):
    def wrapper():
        print("Avant l'appel de la fonction")
        func()
        print("Après l'appel de la fonction")
    return wrapper

@my_decorator
def my_function():
    print("Dans la fonction")

my_function()


"""
Dans cet exemple, on définit un décorateur "my_decorator" qui ajoute un message avant et après l'appel de la fonction. On applique ce décorateur à la fonction "my_function" en utilisant l'annotation "@my_decorator". Lorsque "my_function" est appelée, c'est en fait la fonction "wrapper" qui est appelée, qui appelle ensuite la fonction d'origine "my_function".

"""

# Décorateurs de classe

"""

Les décorateurs peuvent également être utilisés pour modifier le comportement des classes. Voici un exemple de décorateur de classe qui ajoute une méthode statique à une classe existante : """

def add_static_method(cls):
    def my_static_method():
        print("Méthode statique ajoutée !")
    cls.my_static_method = staticmethod(my_static_method)
    return cls

@add_static_method
class MyClass:
    pass

MyClass.my_static_method()


"""

Dans cet exemple, le décorateur "add_static_method" ajoute une méthode statique "my_static_method" à la classe "MyClass". Lorsque "MyClass" est décorée avec ce décorateur, la méthode statique est ajoutée à la classe, et peut être appelée directement à partir de la classe. """



# Cas d'utilisation pratiques

"""

Les décorateurs peuvent être utilisés dans de nombreux cas d'utilisation pratiques. Voici deux exemples :

Mesure du temps d'exécution : on peut créer un décorateur qui mesure le temps d'exécution d'une fonction en utilisant le module "time" de Python. Voici un exemple :

"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Temps d'exécution :", end_time - start_time)
        return result
    return wrapper



# Chapitre 3 : Décorateurs


"""
Les décorateurs sont une fonctionnalité avancée de Python qui permet de modifier le comportement d'une fonction ou d'une méthode sans en modifier le code source. Les décorateurs sont largement utilisés en Python pour ajouter des fonctionnalités supplémentaires à des fonctions existantes, comme la mesure de temps d'exécution, la mise en cache des résultats, l'authentification, etc.

Dans ce chapitre, nous commençons par expliquer le fonctionnement des décorateurs en Python, en montrant comment ils peuvent être utilisés pour modifier le comportement d'une fonction. Nous abordons ensuite la création de ses propres décorateurs, en montrant comment définir une fonction qui prend une autre fonction en argument et renvoie une nouvelle fonction modifiée.

Nous explorons également les décorateurs de classe, qui permettent de modifier le comportement d'une classe entière. Nous montrons comment créer un décorateur de classe, qui prend une classe en argument et renvoie une nouvelle classe modifiée.

Enfin, nous abordons les avantages des décorateurs en matière de modularité, de réutilisabilité et de maintenabilité du code. Nous montrons comment les décorateurs peuvent être utilisés pour ajouter des fonctionnalités à une application de manière modulaire et élégante, et comment ils peuvent améliorer la lisibilité et la maintenabilité du code.


"""

# Fonctionnement des décorateurs

"""
En Python, les décorateurs sont des fonctions qui prennent une autre fonction en argument et renvoient une nouvelle fonction modifiée. La syntaxe pour appliquer un décorateur à une fonction est la suivante :

"""

@decorateur
def fonction():
    ...


"""
L'idée est que la fonction "fonction" est passée au décorateur "decorateur", qui renvoie une nouvelle fonction modifiée. La nouvelle fonction peut ensuite être appelée comme d'habitude.

Voici un exemple de décorateur qui mesure le temps d'exécution d'une fonction :

"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Temps d'exécution :", end_time - start_time, "secondes")
        return result
    return wrapper

@timer
def fonction():
    time.sleep(2)
    return 42

print(fonction())


""""
Dans cet exemple, le décorateur "timer" prend une fonction en argument, mesure le temps d'exécution de cette fonction, puis renvoie une nouvelle fonction qui appelle la fonction d'origine et affiche le temps d'exécution. La fonction "fonction" est décorée avec le décorateur "timer", ce qui permet de mesurer le temps d'exécution de la fonction.

"""

# Création de ses propres décorateurs

""" 
Pour créer un décorateur personnalisé, il suffit de définir une nouvelle fonction qui prend une autre fonction en argument, puis de renvoyer une nouvelle fonction modifiée. Voici un exemple de décorateur qui convertit le résultat d'une fonction en majuscules :

"""

def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result).upper()
    return wrapper

@uppercase
def fonction():
    return "hello, world"

print(fonction())
