"""
La gestion des erreurs et exceptions est un élément essentiel de la programmation.
Les erreurs peuvent survenir pour de nombreuses raisons, comme des entrées utilisateur incorrectes,
 des erreurs de calcul ou des problèmes d'accès aux ressources.
 Les exceptions permettent de détecter ces erreurs et de les traiter de manière appropriée.

Dans ce chapitre, nous commençons par présenter les différents types d'exceptions en Python,
 tels que les exceptions de type "ValueError", "TypeError" ou "FileNotFoundError".
 Nous montrons comment utiliser les blocs "try" et "except" pour intercepter ces exceptions et
 les traiter de manière appropriée.

Nous abordons ensuite la notion de hiérarchie d'exceptions, qui permet de regrouper
les exceptions de manière logique et de simplifier le traitement des erreurs.
Nous montrons comment créer ses propres exceptions en définissant des classes dérivées de la classe "Exception".

Enfin, nous expliquons comment gérer les exceptions de manière élégante en utilisant
 les blocs "finally" et "else", et comment utiliser la clause "with" pour simplifier
 la gestion des ressources telles que les fichiers ouvertures.
"""



# Les blocs try/except

"""
Les blocs "try" et "except" permettent de gérer les erreurs et exceptions en Python. 
Le bloc "try" contient le code qui peut générer une exception, et 
le bloc "except" contient le code qui est exécuté en cas d'exception. Voici un exemple simple :
"""

try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

"""
Dans cet exemple, le bloc "try" demande à l'utilisateur d'entrer un nombre,
 puis divise 10 par ce nombre et affiche le résultat. Si l'utilisateur entre 0,
 une exception de type "ZeroDivisionError" est levée, et le bloc "except" correspondant est exécuté.
"""

# Hiérarchie d'exceptions

"""
La hiérarchie d'exceptions en Python permet de regrouper les exceptions en catégories logiques.
 Par exemple, toutes les exceptions liées aux fichiers sont des sous-classes de la classe "IOError".
 Cela permet de gérer les erreurs de manière plus élégante, en interceptant des exceptions de manière plus générale.
"""

try:
    f = open("myfile.txt")
    contents = f.read()
    f.close()
except IOError:
    print("Error reading file")


"""
Dans cet exemple, le bloc "try" tente d'ouvrir le fichier "myfile.txt", de le lire, puis de le fermer.
 Si une exception de type "IOError" est levée, le bloc "except" correspondant est exécuté.
"""

# Création de ses propres exceptions

"""
Il est possible de créer ses propres exceptions en définissant des classes dérivées de la classe "Exception". 
Cela permet de définir des exceptions spécifiques à un programme ou à une bibliothèque, avec un comportement personnalisé.
"""

class MyException(Exception):
    pass

try:
    raise MyException("This is my exception")
except MyException as e:
    print(e)



#  Chapitre 2 : Gestion des erreurs et exceptions

"""
Les erreurs et exceptions sont des événements indésirables qui peuvent survenir lors de l'exécution d'un programme.
 Python fournit un mécanisme de gestion des erreurs et exceptions qui permet de détecter et de traiter ces événements de manière appropriée.

Dans ce chapitre, nous explorons les types d'exceptions qui peuvent être levées en Python,
 ainsi que les méthodes pour gérer ces exceptions à l'aide des instructions "try" et "except". 
Nous montrons également comment créer nos propres exceptions pour gérer des erreurs spécifiques à notre application.
"""


# Types d'exceptions

"""
Python définit de nombreux types d'exceptions qui peuvent être levées lors de l'exécution d'un programme.
 Les types les plus courants incluent les erreurs de syntaxe ("SyntaxError"), les erreurs de nom ("NameError"), 
 les erreurs d'indice ("IndexError"), les erreurs de type ("TypeError"), 
les erreurs d'attribut ("AttributeError"), les erreurs de division par zéro ("ZeroDivisionError"), etc.
"""

# Gestion des erreurs avec try/except

"""
    L'instruction "try" permet d'essayer d'exécuter un bloc de code qui peut générer une exception, 
    tandis que l'instruction "except" permet de spécifier comment traiter cette exception si elle se produit.
     Voici un exemple de code qui montre comment utiliser "try" et "except" pour gérer une division par zéro :
"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: division by zero")


"""
Dans cet exemple, le bloc de code dans le "try" tente de diviser 10 par 0, ce qui génère une exception de division par zéro. 
Le bloc de code dans le "except" est exécuté pour traiter cette exception, et affiche un message d'erreur.
"""

# Création de ses propres exceptions

"""
Il est parfois nécessaire de créer des exceptions personnalisées pour gérer des erreurs spécifiques à notre application.
 Pour créer une nouvelle exception, on définit une nouvelle classe qui dérive de la classe 
 "Exception" ou d'une de ses sous-classes.
 Voici un exemple de classe qui définit une nouvelle exception pour signaler une erreur d'entrée utilisateur :
"""

class UserInputError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


"""
Dans cet exemple, la classe "UserInputError" définit une nouvelle exception qui dérive de la classe "Exception".
 Le constructeur de la classe prend un message en argument, qui est stocké comme attribut de l'exception. 
La méthode "super().init(message)" appelle le constructeur de la classe parente pour initialiser l'exception.
"""


# Chapitre 2 : Gestion des erreurs et exceptions


"""
La gestion des erreurs est un aspect important de la programmation, qui permet de détecter et
 de gérer les erreurs qui peuvent survenir lors de l'exécution d'un programme. 
Python offre une grande variété d'exceptions intégrées, ainsi que la possibilité 
de créer ses propres exceptions personnalisées.
 Dans ce chapitre, nous examinons les différentes techniques de gestion des erreurs et d'exceptions en Python.

Nous commençons par une présentation des différents types d'exceptions intégrées, tels que la division par zéro,
 l'index hors limites ou l'erreur de syntaxe. Nous montrons comment utiliser la structure try/except
  pour intercepter ces exceptions et gérer les erreurs de manière appropriée.

Nous abordons également la création de ses propres exceptions, en montrant comment créer 
une nouvelle classe d'exception et la lever dans le code. Nous expliquons comment personnaliser
 les messages d'erreur et comment utiliser des exceptions personnalisées pour mieux gérer les erreurs dans un programme.

Enfin, nous discutons des meilleures pratiques pour la gestion des erreurs et exceptions en Python,
 notamment en ce qui concerne la lisibilité, la maintenabilité et la gestion des erreurs imprévues.
"""

# Types d'exceptions intégrées

"""
Python offre de nombreux types d'exceptions intégrées, tels que ZeroDivisionError, IndexError, ValueError, etc.
 Voici un exemple qui illustre comment utiliser la structure try/except pour intercepter une exception IndexError :
"""

my_list = [1, 2, 3]
try:
    print(my_list[3])
except IndexError as e:
    print("Caught an IndexError:", e)


"""
Dans cet exemple, nous essayons d'accéder à un élément de liste qui n'existe pas (index 3),
 ce qui provoque une exception IndexError.
 La structure try/except permet de intercepter cette exception et d'afficher un message d'erreur personnalisé.
"""

# Création de ses propres exceptions

"""
Python permet de créer ses propres exceptions personnalisées, en créant une nouvelle classe qui dérive de la classe Exception. 
Voici un exemple qui montre comment créer une exception personnalisée pour gérer les erreurs de validation :
"""

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def validate_input(value):
    if value < 0:
        raise ValidationError("Input value must be positive")

try:
    validate_input(-1)
except ValidationError as e:
    print("Caught a ValidationError:", e)


"""

Dans cet exemple, nous définissons une nouvelle classe d'exception "ValidationError", 
qui prend un message d'erreur en argument. Nous utilisons ensuite cette exception personnalisée pour 
gérer les erreurs de validation dans la fonction "validate_input".

Meilleures pratiques pour la gestion des erreurs et exceptions
Pour une gestion efficace des erreurs et exceptions en Python, il est important de suivre certaines bonnes pratiques, 
telles que :

Éviter les blocs try/except trop larges qui peuvent masquer des erreurs
Utiliser des messages d'erreur clairs et explicites pour faciliter la compréhension du problème
Éviter de mélanger des exceptions intégrées et personnalisées pour éviter la confusion
Toujours utiliser la forme "except Exception as e" pour éviter de masquer des erre
"""


# Chapitre 2 : Gestion des erreurs et exceptions


"""
Les erreurs et les exceptions sont des situations imprévues qui peuvent survenir lors de l'exécution d'un programme.
 Python fournit un mécanisme pour gérer ces situations et éviter que le programme ne se termine de manière inattendue. 
Ce chapitre explore les types d'exceptions courants en Python et les méthodes pour les gérer.

Nous commençons par présenter les types d'exceptions courants en Python, 
tels que les erreurs de syntaxe, les erreurs de type, les erreurs d'index, etc. 
Nous montrons comment utiliser l'instruction "try/except" pour intercepter ces exceptions et
 exécuter un code de secours en cas d'erreur.

Nous abordons ensuite la création de ses propres exceptions, qui permettent de définir 
des situations d'erreur spécifiques à un programme et de les gérer de manière appropriée.

Enfin, nous discutons des bonnes pratiques de gestion des exceptions, 
telles que la gestion des exceptions spécifiques plutôt que des exceptions génériques,
 la documentation des exceptions et la propagation des exceptions.
"""

# Les types d'exceptions courants en Python

"""
En Python, les exceptions sont des objets qui représentent des erreurs ou des conditions imprévues. 
Voici quelques exemples de types d'exceptions courants en Python :

TypeError : erreur de type d'argument ou d'opérateur
ValueError : valeur d'argument ou de paramètre non valide
IndexError : index ou tranche hors limite
KeyError : clé de dictionnaire non trouvée
AttributeError : attribut inexistant ou non accessible
IOError : erreur d'entrée/sortie
"""

# Utilisation de l'instruction "try/except"

"""
L'instruction "try/except" permet de gérer les exceptions 
en interceptant les erreurs et en exécutant un code de secours en cas d'erreur. 
Voici un exemple d'utilisation de l'instruction "try/except" pour gérer une division par zéro :
"""

try:
    result = x / y
except ZeroDivisionError:
    result = float('inf')


"""
Dans cet exemple, l'instruction "try" tente de diviser "x" par "y". Si "y" est égal à zéro,
 l'exception "ZeroDivisionError" est levée et l'instruction "except" 
est exécutée pour attribuer une valeur infinie à la variable "result".
"""

# Création de ses propres exceptions

"""
La création de ses propres exceptions permet de définir des situations d'erreur spécifiques à
 un programme et de les gérer de manière appropriée.
 Voici un exemple de création d'une exception personnalisée pour une entrée utilisateur invalide :
"""

class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message

try:
    x = int(input("Enter a positive integer: "))
    if x < 0:
        raise InvalidInputError("Input must be positive")
except InvalidInputError as e:
    print(e.message)


"""
Dans cet exemple, la classe "InvalidInputError" est définie pour représenter une erreur d'entrée utilisateur invalide.
 Si l'entrée utilisateur est négative, 
l'exception "InvalidInputError" est levée et l'instruction "except" est exécutée pour afficher le message d'erreur.
"""


# Chapitre 2 : Gestion des erreurs et exceptions

"""
Dans tout programme, il est important de gérer les erreurs qui peuvent se produire pendant l'exécution. Python fournit un système de gestion des exceptions qui permet de détecter et de gérer les erreurs de manière élégante et robuste.

Dans ce chapitre, nous commençons par expliquer les différents types d'exceptions qui peuvent être levées par un programme, 
tels que "ZeroDivisionError", "TypeError" ou "FileNotFoundError". Nous montrons comment utiliser le bloc "try/except" pour intercepter ces exceptions et exécuter un code de secours en cas d'erreur.

Nous montrons également comment créer ses propres exceptions personnalisées, en utilisant la classe "Exception" de Python.

Enfin, nous abordons les notions de blocs "finally" et "else", qui permettent de définir un code à exécuter dans tous les cas, qu'une exception soit levée ou non.
"""

# Le bloc try/except

"""
Le bloc try/except est utilisé pour intercepter les exceptions qui peuvent être levées pendant l'exécution d'un programme. 
Voici un exemple simple qui montre comment utiliser le bloc try/except pour intercepter une division par zéro :
"""

try:
    result = 1 / 0
except ZeroDivisionError:
    print("division by zero!")


"""
Dans cet exemple, la division 1/0 lèvera une exception de type "ZeroDivisionError".
 Le bloc "except" interceptera cette exception et affichera un message d'erreur.
"""

# Création de ses propres exceptions

"""
Python permet de créer ses propres exceptions personnalisées en définissant une nouvelle classe dérivée de "Exception". 
Voici un exemple qui montre comment définir une exception personnalisée pour signaler une erreur de fichier :
"""

class FileError(Exception):
    pass

try:
    with open("nonexistent_file.txt", "r") as f:
        contents = f.read()
except FileNotFoundError:
    raise FileError("file not found!")

"""
Dans cet exemple, nous avons défini une nouvelle classe "FileError" qui dérive de "Exception". 
Dans le bloc try/except, nous essayons d'ouvrir un fichier qui n'existe pas, ce qui lèvera une exception de type "FileNotFoundError". 
Nous utilisons alors le bloc "raise" pour lever notre propre exception "FileError".
"""

# Les blocs finally et else

"""
Les blocs "finally" et "else" sont utilisés pour exécuter un code dans tous les cas,
 qu'une exception soit levée ou non. Le bloc "finally" est souvent utilisé pour libérer des ressources,
  telles que des fichiers ou des connexions réseau. Le bloc "else" est utilisé pour exécuter du code lorsque le bloc try n'a pas levé d'exception.
 Voici un exemple qui montre l'utilisation de ces blocs :
"""

try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("file not found!")
else:
    try:
        contents = f.read()
    except:
        print("error while reading file")
    else:
        print(contents)
finally:
    f.close()

"""
Dans cet exemple, nous essayons d'ouvrir un fichier en lecture. Si le fichier n'existe pas, le bloc "except" affiche un message d'erreur. 
Si le fichier est ouvert avec succès, le bloc "else" lit le contenu du fichier.
"""


# Chapitre 2 : Gestion des erreurs et exceptions

"""
La gestion des erreurs et exceptions est un aspect crucial de la programmation en Python, 
qui permet de traiter les erreurs et les cas imprévus qui peuvent survenir lors de l'exécution d'un programme.
 Dans ce chapitre, nous explorons les types d'exceptions en Python, 
la gestion des erreurs avec try/except, et la création de ses propres exceptions.
"""

# Types d'exceptions

"""
En Python, une exception est une erreur qui se produit lors de l'exécution d'un programme.
 Les exceptions sont représentées par des objets qui contiennent des informations sur l'erreur, 
 telles que le type d'erreur, le message d'erreur et la pile d'appels.
 Python a de nombreux types d'exceptions intégrés, tels que TypeError, ValueError, ZeroDivisionError, etc.
"""

# Gestion des erreurs avec try/except

"""
La gestion des erreurs avec try/except permet de détecter et de gérer les exceptions qui se produisent lors de l'exécution d'un programme.
 La syntaxe try/except est la suivante :
"""

try:
    pass
    #code susceptible de générer une exception
except ExceptionType:
    pass
    #code pour gérer l'exception


"""
Dans cet exemple, le code entre le bloc try et except est susceptible de générer une exception. 
Si une exception de type ExceptionType se produit, 
le bloc except est exécuté pour gérer l'exception.
"""

# Création de ses propres exceptions

"""
En plus des exceptions intégrées, il est possible de créer ses propres exceptions personnalisées en Python. 
Pour créer une exception personnalisée, 
on crée une nouvelle classe dérivée de la classe Exception ou d'une de ses sous-classes. Voici un exemple :
"""

class MyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


"""
Dans cet exemple, la classe MyError est définie comme une sous-classe de la classe Exception.
La classe MyError a deux méthodes : init pour initialiser l'objet et str pour renvoyer une représentation
 sous forme de chaîne de caractères.

En résumé, la gestion des erreurs et exceptions est un aspect important de la programmation en Python.
 En comprenant les types d'exceptions, la gestion des erreurs avec try/except et la création de ses propres exceptions, 
les programmeurs peuvent créer des programmes plus robustes et plus fiables.
"""


"""
La gestion des erreurs est un aspect important de la programmation,
 car elle permet de gérer les cas où quelque chose ne se passe pas comme prévu dans un programme. 
En Python, les erreurs sont gérées à l'aide d'exceptions, qui sont des objets qui représentent des situations
 anormales ou des erreurs. Ce chapitre explore les concepts clés de la gestion des erreurs et des exceptions en Python.

Nous commençons par expliquer les différents types d'exceptions intégrées dans Python,
 tels que la division par zéro, l'index hors limites, etc. Nous montrons comment gérer
  ces exceptions à l'aide de la structure try/except, qui permet de détecter et de traiter
   les exceptions lorsqu'elles se produisent.

Nous abordons également la création de ses propres exceptions, en montrant comment
 définir des classes d'exceptions personnalisées qui peuvent être levées dans des situations spécifiques.

Enfin, nous explorons les bonnes pratiques de gestion des erreurs, en montrant comment capturer et 
logguer les exceptions, et comment utiliser les exceptions pour améliorer la robustesse et la fiabilité des programmes.
"""

# Gestion d'exceptions avec try/except

"""
La structure try/except permet de gérer les exceptions dans un bloc de code. 
Voici un exemple de code qui illustre l'utilisation de try/except pour gérer une division par zéro :
"""
try:
    x = 1 / 0
except ZeroDivisionError:
    print("division by zero")


"""
Dans cet exemple, le code dans le bloc try tente de diviser 1 par zéro, 
ce qui déclenche une exception de type ZeroDivisionError. 
Le bloc except capture cette exception et affiche un message d'erreur approprié
"""

# Création de ses propres exceptions

"""
Pour créer ses propres exceptions, il suffit de définir une nouvelle classe qui dérive de la classe Exception 
ou d'une de ses sous-classes.
 Voici un exemple de code qui illustre la création d'une exception personnalisée :
"""

class MyError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyError("something went wrong")
except MyError as e:
    print(e.message)

"""
Dans cet exemple, la classe MyError est définie comme une sous-classe de Exception.
 La méthode init est utilisée pour initialiser le message d'erreur. 
La commande raise est utilisée pour lever une exception MyError, qui est capturée et gérée dans le bloc except.
"""


"""
Bonnes pratiques de gestion des erreurs
Pour assurer la fiabilité et la robustesse d'un programme, il est important de bien gérer les erreurs. Voici quelques bonnes pratiques à suivre :

Capturer et gérer les exceptions de manière appropriée, en utilisant des blocs try/except.
Éviter les exceptions silencieuses, qui peuvent masquer des erreurs critiques.
Logguer les exceptions pour faciliter le débogage et la maintenance du code.
Utiliser les exceptions pour signaler des erreurs de manière claire et précise.
Éviter de capturer des exceptions génériques comme Exception, qui peuvent masquer des erreurs spécifiques.
"""


# Chapitre 2 : Gestion des erreurs et exceptions

"""
La gestion des erreurs et des exceptions est un aspect essentiel de la programmation,
 car les erreurs peuvent survenir à tout moment lors de l'exécution d'un programme.
  Python offre un mécanisme de gestion d'exceptions robuste et flexible,
   qui permet de gérer les erreurs de manière élégante et efficace.

Dans ce chapitre, nous commençons par expliquer les différents types d'exceptions que Python peut lever,
 et comment les intercepter avec une instruction "try/except". 
 Nous montrons comment utiliser cette instruction pour gérer les erreurs de manière appropriée e
 t fournir des messages d'erreur utiles à l'utilisateur.

Nous abordons également la création de ses propres exceptions, qui permet de créer
 des exceptions personnalisées pour gérer des erreurs spécifiques à une application.
  Nous montrons comment créer une nouvelle classe dérivée de la classe d'exception de base,
   et comment lever cette exception dans le code.

Enfin, nous explorons les avantages de la gestion d'exceptions en matière de sécurité,
 de fiabilité et de maintenabilité du code. Nous montrons comment la gestion d'exceptions
  peut être utilisée pour détecter et gérer les erreurs de manière fiable, 
éviter les comportements imprévus et les failles de sécurité, et améliorer la clarté et la robustesse du code.
"""

# Types d'exceptions et instruction try/except

"""
En Python, les exceptions sont des objets qui représentent des erreurs qui se produisent
 lors de l'exécution du programme. Il existe de nombreux types d'exceptions prédéfinies en Python,
 comme les erreurs de syntaxe, les erreurs d'indexation, les erreurs de type, etc.

Pour gérer les exceptions, on utilise l'instruction "try/except". 
L'idée est de placer le code qui pourrait lever une exception dans un bloc "try",
 et de placer le code de gestion d'exception dans un ou plusieurs blocs "except" 
 correspondants aux différents types d'exceptions.
"""

try:
    x = int(input("Entrez un nombre entier : "))
    y = 10 / x
except ZeroDivisionError:
    print("Erreur : division par zéro !")
except ValueError:
    print("Erreur : valeur incorrecte !")
else:
    print("Le résultat est :", y)


"""
Dans cet exemple, on essaie de diviser 10 par un nombre entier entré par l'utilisateur. 
Si l'utilisateur entre un zéro, une exception de type "ZeroDivisionError" est levée et interceptée 
par le premier bloc "except". Si l'utilisateur entre autre chose qu'un entier, 
une exception de type "ValueError" est levée et interceptée par le deuxième bloc "except". 
Si aucune exception n'est levée, le bloc "else" est exécuté et affiche le résultat de la division.
"""

# Création de ses propres exceptions

"""
Pour créer une exception personnalisée, il suffit de définir une nouvelle classe dérivée de
 la classe d'exception de base (Exception).
 On peut ensuite lever cette exception en utilisant l'instruction "raise". Voici un exemple :
"""

class MyError(Exception):
    pass

try:
    raise MyError("Une erreur s'est produite !")
except MyError as e:
    print("Erreur :", e)
