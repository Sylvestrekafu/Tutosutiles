"""
La programmation orientée objet est un paradigme de programmation qui permet de
modéliser des entités du monde réel sous forme d'objets. Python est un langage orienté objet,
 qui offre des fonctionnalités avancées pour la programmation orientée objet,
 comme l'héritage, le polymorphisme et l'encapsulation.

Dans ce chapitre, nous commençons par expliquer les concepts de base de la programmation orientée objet en Python,
comme les classes, les objets, les attributs et les méthodes. Nous montrons comment définir des classes en Python,
 en utilisant les fonctions spéciales init et repr.

Nous abordons ensuite les concepts avancés de la programmation orientée objet en Python, comme l'héritage,
le polymorphisme et l'encapsulation. Nous montrons comment utiliser ces concepts pour créer des classes et
des objets plus sophistiqués, qui sont plus flexibles, plus réutilisables et plus faciles à maintenir.

Nous explorons également les avantages de la programmation orientée objet en matière de modularité,
 de réutilisabilité et de maintenabilité du code. Nous montrons comment les concepts de
 la programmation orientée objet peuvent être utilisés pour créer des programmes plus structurés, plus faciles à comprendre et plus faciles à maintenir.
"""

# Concepts de base de la programmation orientée objet

"""
Les concepts de base de la programmation orientée objet en Python sont les classes, les objets, 
les attributs et les méthodes. Une classe est une structure de données qui décrit les caractéristiques et
 les comportements d'un ensemble d'objets. Un objet est une instance d'une classe, qui possède des attributs et
  des méthodes spécifiques à cette classe.

Voici un exemple de classe en Python, qui représente un rectangle :
"""

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.longueur, self.largeur)

    def aire(self):
        return self.longueur * self.largeur


"""
Dans cet exemple, on définit une classe Rectangle qui possède deux attributs,
 longueur et largeur, et une méthode aire qui calcule l'aire du rectangle. 
 La méthode init est une fonction spéciale qui est appelée lors de la création d'un nouvel objet de la classe.
 La méthode repr est une fonction spéciale qui retourne une chaîne de caractères représentant l'objet.
"""

# Héritage et polymorphisme

"""
L'héritage et le polymorphisme sont des concepts avancés de la programmation orientée objet en Python,
 qui permettent de créer des classes et des objets plus sophistiqués.
  L'héritage permet de créer des classes qui héritent des attributs et 
  des méthodes d'une classe parente. Le polymorphisme permet à des objets
   de différentes classes d'avoir des comportements similaires.

Voici un exemple de classe qui hérite de la classe Rectangle, en ajoutant une méthode pour calculer le périmètre :
"""

class Carre(Rectangle):
    def __init__(self, cote):
        super().__init__(cote, cote)

    def __repr__(self):
        return "Carre"



# Chapitre 8 : Programmation orientée objet avancée

"""
La programmation orientée objet est un paradigme de programmation qui permet de modéliser des 
concepts du monde réel en utilisant des objets et des classes. Python est un langage de programmation orienté objet,
 et offre des fonctionnalités avancées pour la programmation orientée objet, 
comme l'héritage, la polymorphisme et les classes abstraites.

Dans ce chapitre, nous commençons par expliquer les concepts de base de la programmation orientée objet en Python,
 comme les classes, les objets, les attributs et les méthodes. Nous montrons comment définir des classes 
 et des objets en Python, et comment utiliser les attributs et les méthodes pour manipuler des objets.

Nous abordons ensuite l'héritage, qui est une fonctionnalité avancée de la programmation orientée objet.
 L'héritage permet de créer des classes qui héritent des attributs et des méthodes d'une classe parente, 
 ce qui permet de réutiliser du code et de créer des hiérarchies de classes.

Nous explorons également le polymorphisme, qui permet de manipuler des objets de différentes
 classes de manière uniforme. Le polymorphisme permet de créer des interfaces communes pour des objets
  qui ont des comportements différents.

Enfin, nous abordons les classes abstraites, qui sont des classes qui ne peuvent pas être instanciées directement,
 
 mais qui servent de modèle pour d'autres classes. Les classes abstraites permettent de définir des 
 interfaces communes pour des classes qui ont des comportements différents.
"""

# Concepts de base de la programmation orientée objet

"""
La programmation orientée objet en Python repose sur les concepts de classes, 
d'objets, d'attributs et de méthodes. Une classe est un modèle de données qui définit 
les attributs et les méthodes d'un objet. Un objet est une instance d'une classe, 
qui possède des attributs et des méthodes. Les attributs sont des variables qui stockent des données 
associées à un objet, et les méthodes sont des fonctions qui manipulent les attributs de l'objet.

Voici un exemple de définition d'une classe et de création d'un objet en Python :
"""

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def dire_bonjour(self):
        print("Bonjour, je m'appelle", self.nom, "et j'ai", self.age, "ans")

personne = Personne("Alice", 30)
personne.dire_bonjour()


# Dans cet exemple, on définit une classe Personne qui a deux attributs, nom et age,
# et une méthode dire_bonjour qui affiche le nom et l'âge de la personne.
# On crée ensuite un objet personne en utilisant la classe Personne et on appelle la méthode dire_bonjour sur l'objet.

# Héritage

"""
L'héritage est une fonctionnalité avancée de la programmation orientée objet qui permet 
de créer des classes qui héritent des attributs et des méthodes d'une classe parente.
 L'héritage permet de réutiliser du code et de créer des hiérarchies de classes.

Voici un exemple d'utilisation de l'héritage en Python :
"""

# Chapitre 8 : Programmation orientée objet avancée

"""
La programmation orientée objet (POO) est un paradigme de programmation qui permet de modéliser 
les données et les comportements d'un programme sous forme d'objets. Python est un langage orienté objet,
 qui offre des fonctionnalités avancées pour la POO,
 comme l'héritage, la surcharge d'opérateurs et les décorateurs.

Dans ce chapitre, nous commençons par expliquer les concepts de base de la POO en Python,
 en montrant comment définir des classes et des objets, et comment les utiliser pour encapsuler 
 des données et des comportements.

Nous abordons ensuite l'héritage, qui est un mécanisme clé de la POO en Python. 
Nous montrons comment utiliser l'héritage pour créer des classes dérivées qui héritent 
des propriétés et des comportements des classes de base, et comment surcharger des méthodes
 pour modifier leur comportement.

Nous explorons également la surcharge d'opérateurs, qui est une fonctionnalité avancée
 de la POO en Python. Nous montrons comment surcharger des opérateurs pour créer 
 des classes qui se comportent comme des types de données de base.

Enfin, nous abordons les décorateurs, qui sont des fonctions qui modifient le comportement des
 fonctions et des méthodes. Nous montrons comment utiliser des décorateurs
  pour ajouter des fonctionnalités aux classes et aux méthodes, et comment créer des décorateurs personnalisés.
"""

# Définition de classes et d'objets

"""
La définition de classes et d'objets est le fondement de la POO en Python. Les classes sont des modèles de données
 qui définissent des attributs et des méthodes, tandis que les objets sont des instances
  de classes qui encapsulent des données et des comportements.

Voici un exemple de définition d'une classe "Voiture" en Python, avec des attributs pour la marque,
 le modèle et l'année de fabrication, et des méthodes pour démarrer et arrêter la voiture :
"""

class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.en_marche = False

    def demarrer(self):
        self.en_marche = True
        print("La voiture démarre")

    def arreter(self):
        self.en_marche = False
        print("La voiture s'arrête")


"""
Dans cet exemple, la classe "Voiture" définit des attributs pour la marque, le modèle et l'année de fabrication,
 et des méthodes pour démarrer et arrêter la voiture. La méthode spéciale init est utilisée pour 
initialiser les attributs lors de la création d'une nouvelle instance de la classe.
"""

# Héritage

"""
L'héritage est un mécanisme clé de la POO en Python, qui permet de créer des classes 
dérivées qui héritent des propriétés et des comportements des classes de base. 

Les classes dérivées peuvent surcharger les méthodes des classes de base pour modifier leur comportement,
 ou ajouter de nouvelles méthodes pour étendre leur fonctionnalité.

Voici un exemple de définition d'une classe dérivée "VoitureElectrique" qui hérite de la classe "Voiture" et surcharge
"""

# Chapitre 8 : Programmation orientée objet avancée

"""
La programmation orientée objet est un paradigme de programmation qui permet de structurer 
les programmes en utilisant des objets, qui encapsulent des données et des comportements. 
Python est un langage de programmation 
qui prend en charge la programmation orientée objet, avec des fonctionnalités
 avancées comme l'héritage multiple, les propriétés, les décorateurs et les classes abstraites.

Dans ce chapitre, nous commençons par expliquer les principes de l'héritage multiple, 
qui permet à une classe d'hériter de plusieurs classes parentes. 
Nous montrons comment utiliser l'héritage multiple en Python, en utilisant des exemples concrets.

Nous abordons ensuite les propriétés, qui permettent de définir des accesseurs et des mutateurs
 pour les attributs d'une classe. Nous montrons comment utiliser les propriétés en Python, 
 en utilisant des exemples concrets.

Nous explorons également les décorateurs, qui sont des fonctions qui modifient le
 comportement d'une fonction ou d'une méthode. Nous montrons comment utiliser
  les décorateurs en Python, en utilisant des exemples concrets.

Enfin, nous abordons les classes abstraites, qui sont des classes qui ne peuvent pas être instanciées directement,
 mais qui servent de modèles pour d'autres classes. Nous montrons comment utiliser les classes abstraites en Python,
  en utilisant des exemples concrets.
"""


# Héritage multiple


"""
L'héritage multiple est une fonctionnalité avancée de la programmation orientée objet,
 qui permet à une classe d'hériter de plusieurs classes parentes.
  En Python, l'héritage multiple est géré en utilisant le mécanisme de résolution des conflits,
   qui permet de gérer les conflits entre les méthodes héritées.

Voici un exemple d'utilisation de l'héritage multiple en Python :
"""

class A:
    def methode(self):
        print("Méthode de A")

class B:
    def methode(self):
        print("Méthode de B")

class C(A, B):
    pass

c = C()
c.methode()


"""
Dans cet exemple, on définit deux classes parentes A et B, qui ont chacune une méthode "methode".
 On définit ensuite une classe C qui hérite de A et de B. 
Lorsque la méthode "methode" est appelée sur un objet de la classe C, la méthode héritée de A est appelée.
"""

# Propriétés

"""
Les propriétés sont des fonctions spéciales qui permettent de définir des accesseurs 
et des mutateurs pour les attributs d'une classe. Les accesseurs permettent de lire 
la valeur d'un attribut, tandis que les mutateurs permettent de modifier la valeur d'un attribut.

Voici un exemple d'utilisation de propriétés en Python 
"""

class MaClasse:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valeur):
        self._x = valeur

obj = MaClasse(10)
print(obj.x)
obj.x = 20
print(obj.x)

# Dans cet exemple, on définit une classe MaClasse qui a un attribut x. On définit ensuite deux propriétés pour l


# Chapitre 8 : Programmation orientée objet avancée

"""
La programmation orientée objet est un paradigme de programmation couramment utilisé en Python, 
qui permet de modéliser des concepts du monde réel sous forme d'objets et de classes.
 Python offre une syntaxe simple et élégante pour la programmation orientée objet,
 qui permet de créer des classes et des objets avec peu de code.

Dans ce chapitre, nous commençons par expliquer les concepts avancés de la programmation orientée objet,
 tels que l'héritage, la polymorphie et l'encapsulation.
  Nous montrons comment utiliser ces concepts pour créer des hiérarchies de classes sophistiquées,
   qui peuvent être utilisées pour modéliser des problèmes complexes.

Nous abordons également les décorateurs, qui sont des fonctions qui permettent de modifier 
le comportement des méthodes d'une classe. Les décorateurs peuvent être utilisés pour ajouter
 des fonctionnalités aux méthodes, pour effectuer des vérifications de préconditions et de postconditions,
  ou pour implanter des modèles de conception courants.

Enfin, nous explorons les avantages de la programmation orientée objet en matière de modularité,
 de réutilisabilité et de maintenabilité du code. Nous montrons comment les concepts de la programmation 
 orientée objet peuvent être utilisés pour créer des bibliothèques et des frameworks réutilisables, et
  comment ils peuvent faciliter la maintenance du code à long terme.
"""

# Concepts avancés de la programmation orientée objet

"""
Les concepts avancés de la programmation orientée objet comprennent l'héritage,
 la polymorphie et l'encapsulation. L'héritage permet de définir des classes qui héritent des propriétés et
  des méthodes d'autres classes. La polymorphie permet de traiter des objets 
  de différentes classes de manière uniforme. L'encapsulation permet de cacher les détails 
  d'implémentation d'une classe derrière une interface publique.

Voici un exemple de hiérarchie de classes en utilisant l'héritage en Python :
"""

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        raise NotImplementedError("Méthode non implémentée")

class Chat(Animal):
    def parler(self):
        return "Miaou"

class Chien(Animal):
    def parler(self):
        return "Ouaf"

animaux = [Chat("Félix"), Chien("Médor")]
for animal in animaux:
    print(animal.nom + " : " + animal.parler())


"""
Dans cet exemple, on définit une classe Animal de base qui a une méthode parler non implémentée.
 On définit ensuite deux classes dérivées, Chat et Chien, qui implémentent la méthode parler de manière différente.
  On crée des instances de ces classes et on les ajoute à une liste d'animaux. 
On utilise ensuite une boucle pour parcourir la liste d'animaux et appeler la méthode parler de chaque animal.
"""

# Décorateurs

"""
Les décorateurs sont des fonctions qui permettent de modifier le comportement des méthodes d'une classe. 
Les décorateurs peuvent être utilisés pour ajouter des fonctionnalités aux méthodes,
 pour effectuer des vérifications de préconditions et de postconditions, 
ou pour implanter des modèles de conception courants.
"""
# Chapitre 8 : Programmation orientée objet avancée


"""
La programmation orientée objet est un paradigme de programmation qui permet de structurer un programme 
en utilisant des objets, qui représentent des entités du monde réel. 
Python est un langage de programmation qui supporte la programmation orientée objet, et
 offre une syntaxe élégante et concise pour la création et la manipulation d'objets.

Dans ce chapitre, nous abordons la programmation orientée objet avancée en Python, 
en montrant comment créer des classes et des objets, et comment utiliser 
les concepts avancés de la programmation orientée objet, comme l'héritage, la polymorphie et les décorateurs.

Nous montrons également comment utiliser les modules de la bibliothèque 
standard pour créer des classes et des objets sophistiqués, comme les threads, les queues et les événements.

Enfin, nous explorons les avantages de la programmation orientée objet en matière 
de modularité, de maintenabilité et de réutilisabilité du code. Nous montrons comment
 la programmation orientée objet peut aider à structurer le code de manière claire 
 et efficace, et comment elle peut faciliter la maintenance et l'évolution du code à long terme.
"""

# Création de classes et d'objets

"""
La création de classes et d'objets est l'un des aspects fondamentaux de la programmation orientée objet en Python.
 Une classe est une structure qui définit les propriétés et les comportements d'un ensemble d'objets,
  tandis qu'un objet est une instance d'une classe.

Voici un exemple de création d'une classe Personne en Python :
"""
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher(self):
        print("Je m'appelle", self.nom, "et j'ai", self.age, "ans")

p1 = Personne("Alice", 30)
p2 = Personne("Bob", 25)

p1.afficher()
p2.afficher()


"""
Dans cet exemple, on crée une classe Personne qui a deux propriétés, nom et age, e
t une méthode afficher qui affiche le nom et l'âge d'une personne.
 On crée ensuite deux objets de type Personne, p1 et p2, et
 on appelle la méthode afficher pour afficher les informations de chaque personne.
"""

# Héritage et polymorphie

"""
L'héritage et la polymorphie sont des concepts avancés de la programmation orientée objet en Python.
 L'héritage permet de créer des classes dérivées à partir de classes existantes,
  en héritant des propriétés et des comportements de la classe de base. 
  La polymorphie permet de créer des objets qui peuvent être utilisés de manière interchangeable,
   en utilisant une interface commune.

Voici un exemple de création d'une classe dérivée Employe, qui hérite des propriétés 
et des comportements de la classe Personne :
"""

class Employe(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self.salaire = salaire

    def afficher(self):
        super().afficher()
        print("Mon salaire est de", self.salaire, "euros")

e1 = Employe("Alice", 30, 3000)
e2 = Employe("Bob", 25)
