"""
Définition d'une classe
La définition d'une classe se fait en utilisant le mot-clé class, suivi du nom de la classe (en CamelCase).
On peut également définir un constructeur (méthode spéciale __init__) pour initialiser les attributs de la classe :
"""

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


"""
Dans cet exemple, nous avons créé une classe Personne avec deux attributs (nom et age) 
et un constructeur qui prend en argument le nom et l'âge d'une personne et initialise les attributs correspondants.
"""

#***********************************************************************
#Création d'un objet
# Pour créer un objet à partir d'une classe, on utilise le nom de la classe suivi de parenthèses :
#************************************************************************

p1 = Personne("Alice", 25)

#Dans cet exemple, nous avons créé un objet p1 de la classe Personne avec le nom "Alice" et l'âge 25.

#***********************************************************************
#Héritage
#L'héritage permet de créer une nouvelle classe à partir d'une classe existante,
# en ajoutant des attributs et des méthodes supplémentaires ou en redéfinissant ceux existants. Voici un exemple :
#***********************************************************************

class Etudiant(Personne):
    def __init__(self, nom, age, matricule):
        super().__init__(nom, age)
        self.matricule = matricule

    def afficher_matricule(self):
        print("Matricule :", self.matricule)


"""
Dans cet exemple, nous avons créé une classe Etudiant qui hérite de la classe Personne.
Nous avons redéfini le constructeur 
pour ajouter un nouvel attribut matricule et créé une nouvelle méthode afficher_matricule.
"""


#*****************************************************************

#Polymorphisme
#Le polymorphisme permet à des objets de classes différentes d'avoir des comportements similaires
# en utilisant des méthodes avec le même nom. Voici un exemple :
#*****************************************************************

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def faire_du_bruit(self):
        print("Je fais du bruit !")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Miaou !")

class Chien(Animal):
    def faire_du_bruit(self):
        print("Ouaf !")

animaux = [Chat("Félix"), Chien("Médor")]
for animal in animaux:
    animal.faire_du_bruit()



"""
Dans cet exemple, nous avons créé une classe Animal avec une méthode faire_du_bruit qui affiche "Je fais du bruit !". 
Nous avons créé deux sous-classes Chat et Chien qui redéfinissent la méthode faire_du_bruit avec des comportements différents. 
Enfin, nous avons créé une liste d'animaux et appelé la méthode faire_du_bruit pour chaque animal,
 ce qui produit la sortie suivante :
    Miaou !
    Ouaf !

"""


#Exemple 1 : création d'une classe en Python

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self):
        print("Bonjour, je m'appelle", self.nom, "et j'ai", self.age, "ans.")

"""
Dans cet exemple, nous créons une classe Personne qui a deux attributs (nom et age) et
 une méthode (parler). L'attribut self fait référence à l'objet en cours de création.
"""

#Exemple 2 : utilisation de l'héritage en Python

class Employe(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self.salaire = salaire

    def travailler(self):
        print("Je travaille dur pour gagner", self.salaire, "euros par mois.")


"""
Dans cet exemple, nous créons une classe Employe qui hérite de la classe Personne.
 La méthode __init__ de la classe Employe utilise la méthode __init__ de la classe Personne en appelant la fonction super(). 
La classe Employe a également une méthode supplémentaire (travailler) qui affiche le salaire de l'employé.
"""

#Exemple 3 : utilisation de méthodes spéciales en Python

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self):
        return "Rectangle de longueur {} et de largeur {}".format(self.longueur, self.largeur)

    def __eq__(self, other):
        return self.longueur == other.longueur and self.largeur == other.largeur



"""
Dans cet exemple, nous créons une classe Rectangle qui a deux attributs (longueur et largeur). Nous utilisons la méthode spéciale __str__ pour afficher une représentation textuelle de l'objet. Nous utilisons également la méthode spéciale __eq__ pour comparer deux objets de la classe Rectangle 
en fonction de leur longueur et de leur largeur.

Ces exemples montrent comment la POO peut être utilisée pour créer des structures de 
données complexes et organiser le code en modules réutilisables. La POO permet de créer des classes
 dérivées à partir de classes existantes et de personnaliser le comportement des méthodes en fonction des besoins.
"""


# Création d'une classe

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, message):
        print(f"{self.nom} dit : {message}")


"""
Dans cet exemple, nous définissons une classe
Personne avec un constructeur qui prend deux arguments : nom et age.
 Nous définissons également une méthode parler qui prend un message en argument et l'affiche à l'écran avec le nom de la personne qui parle.
"""

# Création d'une classe dérivée

class Etudiant(Personne):
    def __init__(self, nom, age, matiere):
        super().__init__(nom, age)
        self.matiere = matiere

    def etudier(self):
        print(f"{self.nom} étudie {self.matiere}")


"""
Dans cet exemple, nous définissons une classe Etudiant qui hérite de la classe Personne. 
La classe Etudiant a un constructeur qui prend un argument supplémentaire matiere.
 Nous définissons également une méthode etudier qui affiche à l'écran ce que l'étudiant étudie.
"""

# Redéfinition de méthodes

class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Carre(Rectangle):
    def __init__(self, cote):
        super().__init__(cote, cote)



"""
Dans cet exemple, nous définissons une classe Rectangle avec une méthode aire qui calcule l'aire du rectangle.
 Nous définissons ensuite une classe Carre qui hérite de la classe Rectangle et qui a un constructeur qui prend un seul argument cote. Dans cette classe Carre, nous redéfinissons la méthode __init__ pour initialiser les valeurs de largeur et hauteur à la valeur de cote. Nous n'avons pas besoin de redéfinir la méthode aire, car elle fonctionnera toujours correctement pour un carré.
"""


# Utilisation de méthodes spéciales

class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def __add__(self, autre_fraction):
        nouveau_numerateur = self.numerateur * autre_fraction.denominateur + autre_fraction.numerateur * self.denominateur
        nouveau_denominateur = self.denominateur * autre_fraction.denominateur
        return Fraction(nouveau_numerateur, nouveau_denominateur)

    def __str__(self):
        return f"{self.numerateur}/{self.denominateur}"



"""
Dans cet exemple, nous définissons une classe Fraction avec une méthode spéciale __add__,
 qui permet de définir le comportement de l'addition pour les objets de la classe Fraction.
 Nous redéfinissons également la méthode __str__, qui permet de définir la représentation 
 sous forme de chaîne de caractères des objets de la classe Fraction.
"""



# Exemple 1 : Création d'une classe et d'un objet

"""
Nous allons créer une classe simple pour représenter un point dans l'espace en 3 dimensions. 
La classe aura trois attributs : x, y et z, qui représentent les coordonnées du point.
 Nous allons également définir une méthode pour afficher les coordonnées du point.
"""


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def afficher(self):
        print(f"({self.x}, {self.y}, {self.z})")


"""
Maintenant que nous avons défini notre classe, 
nous pouvons créer un objet Point3D en fournissant des valeurs pour les coordonnées :
"""

p = Point3D(1, 2, 3)
p.afficher()  # Affiche "(1, 2, 3)"

# Exemple 2 : Héritage et polymorphisme


"""
Nous allons maintenant créer une classe dérivée de Point3D, appelée Point4D, 
qui représente un point dans l'espace en 4 dimensions. Nous allons ajouter un quatrième attribut, w,
 qui représente la coordonnée supplémentaire, 
et redéfinir la méthode afficher pour prendre en compte la coordonnée supplémentaire.
"""


class Point4D(Point3D):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self.w = w

    def afficher(self):
        print(f"({self.x}, {self.y}, {self.z}, {self.w})")


"""
Maintenant que nous avons défini notre classe dérivée, nous pouvons créer un objet Point4D et appeler la méthode afficher :

python
"""

p = Point4D(1, 2, 3, 4)
p.afficher()  # Affiche "(1, 2, 3, 4)"

"""
Notez que la méthode afficher de la classe dérivée remplace la méthode afficher de la classe de base, 
ce qui est un exemple de polymorphisme.
"""

# Exemple 3 : Méthodes spéciales

"""
Les méthodes spéciales sont des méthodes prédéfinies en Python qui permettent de personnaliser le comportement des objets pour certaines opérations. Par exemple, 
la méthode add permet de définir l'addition entre deux objets.

Nous allons ajouter une méthode spéciale add à notre classe Point3D pour permettre d'additionner deux points.
 L'addition de deux points se fait simplement en ajoutant les coordonnées correspondantes.
"""


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3D(x, y, z)

    def afficher(self):
        print(f"({self.x}, {self.y}, {self.z})")


# Maintenant que nous avons défini la méthode add, nous pouvons ajouter deux objets Point



# Définition d'une classe simple
"""
Pour créer une classe, on utilise le mot-clé "class" suivi du nom de la classe, suivi de ":". 
Voici un exemple de classe simple qui représente un point dans un plan cartésien :
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5



"""
Dans cet exemple, la classe "Point" a deux attributs : "x" et "y". 
Le constructeur de la classe ("init") prend deux arguments qui sont utilisés pour initialiser les attributs.
 La méthode "distance_from_origin" calcule la distance du point à l'origine du plan.
 
"""

# Héritage et polymorphisme

"""
L'héritage permet de créer une nouvelle classe dérivée d'une classe existante, 
en réutilisant les attributs et les méthodes de la classe parente. 
Le polymorphisme permet à une méthode de s'adapter à différentes classes dérivées ayant des comportements différents. 
Voici un exemple qui illustre ces concepts :
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

animals = [Dog("Fido"), Cat("Whiskers"), Dog("Rex")]
for animal in animals:
    print(animal.name, animal.speak())



"""
Dans cet exemple, la classe "Animal" est la classe parente, qui définit une méthode abstraite "speak". 
Les classes dérivées "Dog" et "Cat" redéfinissent cette méthode pour produire des sons différents.
 La boucle for crée une liste d'animaux de différents types,
 et utilise la méthode "speak" pour produire leur son caractéristique.
"""

# Méthodes spéciales

"""
Les méthodes spéciales permettent de personnaliser le comportement de certains opérateurs ou fonctions intégrées en Python.
 Voici un exemple de classe qui redéfinit 
les méthodes spéciales "add" et "str" pour permettre l'addition et l'affichage de fractions :
"""

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.denominator * other.denominator
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return Fraction(new_numerator, common_denominator)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)


"""
Dans cet exemple, la méthode spéciale "add" permet d'additionner deux fractions, en créant une nouvelle fraction avec un dénominateur commun.
 La méthode "str" permet d'afficher une fraction sous la forme d'une chaîne de caractères.
"""