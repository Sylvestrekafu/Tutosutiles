"""
La manipulation de fichiers et de données est un aspect important de la programmation, qui permet de lire et d'écrire des données à partir de fichiers ou d'autres sources de données. Python offre une bibliothèque standard pour la manipulation de fichiers et de données, qui permet de lire et d'écrire des fichiers, des bases de données et d'autres sources de données.

Dans ce chapitre, nous commençons par expliquer comment ouvrir, lire et écrire des fichiers en Python, en montrant comment utiliser les fonctions built-in de Python pour manipuler des fichiers. Nous abordons ensuite la manipulation de bases de données, en montrant comment utiliser la bibliothèque SQLite pour créer, lire et écrire des bases de données.

Nous explorons également les formats de données courants en Python, tels que JSON et CSV, et comment les lire et les écrire à l'aide des bibliothèques correspondantes. Nous montrons comment manipuler des données structurées et semi-structurées à l'aide de ces formats de données.

Enfin, nous abordons les avantages de la manipulation de fichiers et de données en matière de stockage, de traitement et d'analyse de données. Nous montrons comment la manipulation de fichiers et de données peut être utilisée pour stocker, traiter et analyser des données de manière efficace et élégante.
"""

# Manipulation de fichiers

"""
La manipulation de fichiers en Python est réalisée à l'aide de fonctions built-in telles que "open", "read" et "write". Voici un exemple qui montre comment ouvrir un fichier, lire son contenu et écrire un nouveau contenu dans le même fichier :

"""

with open("mon_fichier.txt", "r") as f:
    contenu = f.read()
    print(contenu)

with open("mon_fichier.txt", "w") as f:
    f.write("Nouveau contenu")

"""
Dans cet exemple, on ouvre le fichier "mon_fichier.txt" en mode lecture, on lit son contenu avec la fonction "read" et on l'affiche.
 Ensuite, on ouvre le même fichier en mode écriture, on écrit un nouveau contenu avec la fonction "write".
"""

# Manipulation de bases de données

"""
La manipulation de bases de données en Python est réalisée à l'aide de la bibliothèque SQLite, qui est une bibliothèque de base de données légère et intégrée à Python. 
Voici un exemple qui montre comment créer une base de données, insérer des données et les récupérer :
"""
import sqlite3

conn = sqlite3.connect("ma_base_de_donnees.db")

c = conn.cursor()

c.execute('''CREATE TABLE utilisateurs
             (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, age INTEGER)''')

c.execute("INSERT INTO utilisateurs VALUES (1, 'Dupont', 'Jean', 30)")
c.execute("INSERT INTO utilisateurs VALUES (2, 'Martin', 'Pierre', 40)")

conn.commit()

c.execute("SELECT * FROM utilisateurs")

resultats = c.fetchall()

for resultat in resultats:
    print(resultat)

conn.close()

"""
Dans cet exemple, on crée une base de données SQLite, on crée une table "utilisateurs", 
on insère deux enregistrements dans la table et on les récupère avec une requête SELECT.
 La base de données est ensuite fermée.
"""


# Chapitre 6 : Manipulation de fichiers et de données

"""
La manipulation de fichiers et de données est une tâche courante en programmation,
 qui consiste à lire et écrire des fichiers, à manipuler des données en mémoire,
  et à communiquer avec des bases de données.
 Python offre une bibliothèque standard pour la manipulation de fichiers et de données, 
 qui permet de gérer les opérations de manière élégante et efficace.

Dans ce chapitre, nous commençons par expliquer comment ouvrir, lire et écrire des fichiers en Python,
 en montrant comment utiliser les fonctions intégrées pour manipuler des fichiers de différents types.
  Nous abordons ensuite la manipulation de données en mémoire, en montrant comment utiliser les structures 
  de données intégrées pour stocker et manipuler des données.

Nous explorons également la communication avec des bases de données en Python, en montrant comment 
utiliser des bibliothèques tierces pour se connecter à des bases de données, exécuter des requêtes et 
récupérer les résultats. Nous abordons également les avantages de la manipulation de fichiers et de 
données en matière de fiabilité, de performance et de maintenabilité du code.
"""

# Manipulation de fichiers


"""
La manipulation de fichiers en Python consiste à ouvrir, lire et écrire des fichiers de différents types, 
comme des fichiers texte, CSV, JSON, XML, etc. Python offre des fonctions intégrées pour manipuler ces types de fichiers de manière élégante et efficace.

Voici un exemple de programme qui lit un fichier texte et affiche son contenu :
"""

with open("mon_fichier.txt", "r") as f:
    contenu = f.read()
    print(contenu)


"""
Dans cet exemple, la fonction "open" est utilisée pour ouvrir un fichier en mode lecture, puis la fonction "read" est utilisée pour lire le contenu du fichier.
 Le mot-clé "with" est utilisé pour s'assurer que le fichier est correctement fermé après son utilisation.
"""

# Manipulation de données en mémoire

"""
La manipulation de données en mémoire en Python consiste à utiliser les structures de données 
intégrées pour stocker et manipuler des données, comme les listes, les dictionnaires, les ensembles, etc. Ces structures de données permettent de manipuler les données de manière élégante et efficace.

Voici un exemple de programme qui utilise une liste pour stocker des nombres entiers, puis calcule leur somme :
"""

nombres = [1, 2, 3, 4, 5]
somme = sum(nombres)
print(somme)


"""
Dans cet exemple, la liste 
"nombres" est utilisée pour stocker des nombres entiers, puis la fonction "sum" est utilisée pour calculer leur somme.
"""

# Communication avec des bases de données

"""
La communication avec des bases de données en Python consiste à utiliser des bibliothèques 
tierces pour se connecter à des bases de données, 
exécuter des requêtes et récupérer les résultats. Python offre de nombreuses bibliothèques pour 
communiquer avec des bases de données, comme psycopg2 pour les bases de données PostgreSQL,
 mysql-connector-python pour les bases de données MySQL, etc.

Voici un exemple de programme qui se connecte à une base de données PostgreSQL,
 exécute une requête SQL pour récupérer les noms des tables, et affiche les résultats :
"""

# Chapitre 6 : Manipulation de fichiers et de données

"""
La manipulation de fichiers et de données est une partie essentielle de la programmation. 
Python offre de nombreuses fonctionnalités pour lire et écrire des fichiers, 
manipuler des données structurées, et stocker des données dans des formats de fichiers standard.

Dans ce chapitre, nous commençons par expliquer les différentes méthodes pour lire et écrire des fichiers en Python,
 en montrant comment utiliser les fonctions prédéfinies pour ouvrir, lire et écrire des fichiers.

Nous abordons ensuite la manipulation de données structurées en Python, en montrant comment utiliser 
les bibliothèques standard pour gérer des données tabulaires, comme les CSV et les feuilles de calcul.

Nous explorons également les avantages de la manipulation de fichiers et de données en Python en matière de fiabilité, de flexibilité et de facilité d'utilisation. Nous montrons comment les fonctionnalités de manipulation de fichiers et de données de Python peuvent aider à automatiser des tâches, à gérer des données volumineuses,
 et à améliorer l'efficacité de la programmation.
"""

# Lecture et écriture de fichiers

"""
Python offre des fonctionnalités intégrées pour lire et écrire des fichiers. Pour lire un fichier, 
on utilise la fonction "open" pour ouvrir le fichier en mode lecture, puis la méthode "read" pour lire le contenu du fichier. Pour écrire un fichier, on utilise la fonction "open" pour ouvrir le fichier en mode écriture, puis la méthode "write" pour écrire le contenu dans le fichier.

Voici un exemple de code qui lit le contenu d'un fichier et l'affiche à l'écran :
"""

with open("fichier.txt", "r") as f:
    contenu = f.read()
    print(contenu)

# Dans cet exemple, on utilise la fonction "open" pour ouvrir le fichier "fichier.txt" en mode lecture.
# On utilise ensuite la méthode "read" pour lire le contenu du fichier dans une variable "contenu".
# Enfin, on affiche le contenu à l'écran avec la fonction "print".

# Manipulation de données structurées

"""
Python offre des bibliothèques standard pour la manipulation de données structurées, 
comme les CSV et les feuilles de calcul. La bibliothèque csv permet de lire et d'écrire des fichiers CSV, tandis que la bibliothèque openpyxl permet de lire et d'écrire des fichiers Excel.

Voici un exemple de code qui lit un fichier CSV et affiche son contenu à l'écran :
"""

import csv

with open("fichier.csv", "r") as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        print(ligne)

# Dans cet exemple, on utilise la bibliothèque csv pour lire le fichier CSV "fichier.csv".
# On utilise la fonction "reader" pour créer un objet lecteur,
# puis on itère sur les lignes du fichier avec une boucle for.

# Stockage de données dans des formats de fichiers standard

"""
Python offre également des bibliothèques standard pour stocker des données dans des formats de fichiers standard,
 comme les JSON et les pickle. La bibliothèque json permet de stocker des données dans le format JSON,
  tandis que la bibliothèque pickle permet de stocker des objets Python dans un format binaire.

Voici un exemple de code qui stocke des données dans un fichier JSON :
"""

# Chapitre 6 : Manipulation de fichiers et de données

"""
La manipulation de fichiers et de données est une tâche courante en programmation,
 qui permet de lire et d'écrire des données à partir de fichiers et d'autres sources de données.
  Python offre des fonctionnalités avancées pour la manipulation de fichiers et de données,
 qui permettent de gérer des formats de données complexes, comme les fichiers CSV, JSON, XML, etc.

Dans ce chapitre, nous commençons par expliquer les différents types de fichiers et de formats 
de données que Python peut gérer, et comment les lire et les écrire à
 l'aide de fonctions de la bibliothèque standard de Python.

Nous abordons ensuite la manipulation de données structurées, comme les fichiers CSV, JSON et XML,
 en montrant comment lire et écrire ces formats de données en Python. 
 Nous explorons également les avantages de la manipulation de fichiers et 
 de données en matière de traitement de données, d'analyse de données et de stockage de données.
"""

# Lecture et écriture de fichiers

"""
En Python, la lecture et l'écriture de fichiers est un processus simple,
 qui utilise des fonctions de la bibliothèque standard de Python, comme "open", "read" et "write". 
Voici un exemple de code qui lit un fichier texte et affiche son contenu :
"""

with open("mon_fichier.txt", "r") as f:
    contenu = f.read()
    print(contenu)

"""
Dans cet exemple, on ouvre un fichier texte en mode lecture, et on lit son contenu à l'aide de la fonction "read".
 La clause "with" est utilisée pour s'assurer que le fichier est correctement fermé après son utilisation.

Voici un exemple de code qui écrit un fichier texte :
"""

with open("mon_fichier.txt", "w") as f:
    f.write("Bonjour, monde !")


"""
Dans cet exemple, on ouvre un fichier texte en mode écriture, 
et on écrit une chaîne de caractères à l'aide de la fonction "write".
"""

# Manipulation de données structurées

"""
Python offre des fonctionnalités avancées pour la manipulation de données structurées,
 comme les fichiers CSV, JSON et XML. Pour lire et écrire ces formats de données,
  on utilise des modules spécifiques de la bibliothèque standard de Python, comme csv, json et xml.etree.ElementTree.

Voici un exemple de code qui lit un fichier CSV et affiche son contenu :
"""

import csv

with open("mon_fichier.csv", "r") as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        print(ligne)


"""
Dans cet exemple, on ouvre un fichier CSV en mode lecture, et on utilise la fonction "csv.reader" pour lire son contenu. 
La boucle "for" est utilisée pour afficher chaque ligne du fichier.

Voici un exemple de code qui écrit un fichier CSV :

"""
import csv

donnees = [
    ["Nom", "Age", "Ville"],
    ["Alice", 25, "Paris"],
    ["Bob", 30, "Lyon"],
    ["Charlie", 35, "Marseille"]
]

with open("mon_fichier.csv", "w", newline="") as f:
    ecrivain = csv.writer(f)
    for ligne in donnees:
        ecrivain.writerow(ligne)


# Chapitre 6 : Manipulation de fichiers et de données

"""
La manipulation de fichiers et de données est une tâche courante en programmation,
 qui consiste à lire et écrire des fichiers, à manipuler des données structurées
  comme des tableaux et des dictionnaires, et à stocker des données dans des bases de données. Python offre une bibliothèque standard complète pour la manipulation de fichiers et de données,
 qui permet de réaliser ces tâches de manière élégante et efficace.

Dans ce chapitre, nous commençons par expliquer les différentes méthodes pour
 lire et écrire des fichiers en Python, en montrant comment ouvrir un fichier,
  lire son contenu et écrire dans le fichier. Nous abordons également les formats 
  de fichiers courants en Python, comme les fichiers CSV et les fichiers JSON, 
  qui permettent de stocker et d'échanger des données structurées.

Nous explorons ensuite les structures de données courantes en Python, comme les tableaux 
et les dictionnaires, et montrons comment manipuler ces structures pour stocker et traiter des données.
 Nous abordons également les modules de manipulation de données courants en Python, 
 comme Pandas, qui permettent de manipuler des données structurées de manière efficace.

Enfin, nous abordons les avantages de la manipulation de fichiers et de données en matière de traitement des données,
 de visualisation des données et de maintenabilité du code. Nous montrons comment la manipulation de fichiers et de données peut être utilisée pour stocker et traiter des données de manière efficace, et comment elle peut faciliter la maintenance et la réutilisation du code.
"""


# Lecture et écriture de fichiers

"""
En Python, on peut lire et écrire des fichiers en utilisant les fonctions prédéfinies open(), read() et write().
 Pour lire un fichier, on ouvre le fichier avec open() et on lit son contenu avec read(). 
Pour écrire dans un fichier, on ouvre le fichier avec open() en mode écriture,
 et on écrit dans le fichier avec write().
"""

# Voici un exemple de programme qui lit le contenu d'un fichier texte et l'affiche à l'écran :

with open("mon_fichier.txt", "r") as f:
    contenu = f.read()
    print(contenu)

"""
Dans cet exemple, on ouvre le fichier "mon_fichier.txt" en mode lecture avec open(),
 on lit son contenu avec read(), puis on affiche le contenu à l'écran.

Voici un exemple de programme qui écrit dans un fichier texte :
"""

with open("mon_fichier.txt", "w") as f:
    f.write("Bonjour, monde !\n")
    f.write("Comment allez-vous ?\n")


"""
Dans cet exemple, on ouvre le fichier "mon_fichier.txt" 
en mode écriture avec open(), on écrit dans le fichier avec write(), puis on ferme le fichier avec le bloc with.
"""

# Formats de fichiers courants

"""
En Python, il existe de nombreux formats de fichiers courants pour stocker et échanger des données structurées.
 Parmi les formats courants, on trouve les fichiers CSV, les fichiers JSON, les fichiers XML et les fichiers YAML.

Le format CSV (Comma-Separated Values) est un format de fichier qui stocke des données tabulaires, 
comme des tableaux. Les données sont séparées par des virgules, et chaque ligne représente un enregistrement.

Le format JSON (JavaScript Object Notation
"""

# Chapitre 6 : Manipulation de fichiers et de données

"""
La manipulation de fichiers et de données est une tâche courante de la programmation, 
qui consiste à lire et écrire des données dans des fichiers, des bases de données ou 
des flux de données. Python offre une bibliothèque standard complète pour la manipulation de fichiers et de données, 
qui permet de lire et écrire des fichiers de différents formats, d'interroger des bases de
 données et de traiter des flux de données.

Dans ce chapitre, nous commençons par expliquer les différents formats de fichiers 
couramment utilisés en Python, comme les fichiers texte,
 les fichiers CSV, les fichiers JSON et les fichiers XML. Nous montrons comment 
 lire et écrire des données dans ces différents formats, en utilisant les modules de la bibliothèque standard.

Nous abordons également la manipulation de bases de données en Python, 
en montrant comment interroger des bases de données SQL en utilisant 
le module sqlite3 de la bibliothèque standard.

Enfin, nous explorons les avantages de la manipulation de fichiers et 
de données en matière de traitement de données, de stockage de données et de portabilité du code.
 Nous montrons comment les modules de la bibliothèque standard peuvent être 
 utilisés pour traiter des données de manière efficace et portable, et 
 comment ils peuvent améliorer la productivité et la qualité du code.
"""

# Lecture et écriture de fichiers

"""
Python offre des fonctionnalités complètes pour la lecture et l'écriture de fichiers de différents formats.
 Les fichiers texte, les fichiers CSV, les fichiers JSON et les fichiers XML sont des formats 
 couramment utilisés en Python, et Python offre des modules pour lire et écrire des données dans ces formats.

Voici un exemple de lecture et d'écriture de données dans un fichier CSV :
"""

import csv

with open("donnees.csv", "r") as f:
    reader = csv.reader(f)
    for ligne in reader:
        print(ligne)

with open("resultats.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["nom", "age", "ville"])
    writer.writerow(["Alice", 30, "Paris"])
    writer.writerow(["Bob", 25, "Lyon"])
    writer.writerow(["Charlie", 35, "Marseille"])


"""
Dans cet exemple, on lit les données d'un fichier CSV avec le module csv et on affiche chaque ligne.
 On écrit ensuite des données dans un fichier CSV en utilisant le module csv et la fonction writerow pour
  écrire chaque ligne.
"""

# Manipulation de bases de données

"""
Python offre également des fonctionnalités pour interroger des bases de données SQL 
en utilisant le module sqlite3 de la bibliothèque standard. Le module sqlite3 permet 
de se connecter à une base de données SQLite et d'interroger la base de données en utilisant des requêtes SQL.

Voici un exemple de connexion à une base de données SQLite et d'exécution d'une requête SQL :
"""

import sqlite3

connexion = sqlite3.connect("ma_base_de_donnees.db")
curseur = connexion.cursor()
curseur.execute("SELECT * FROM utilisateurs")
resultats = curseur.fetchall()
for resultat in resultats:
    print(resultat)
connexion.close()


"""
Dans cet exemple, on se connecte à une base de données SQLite en utilisant la fonction connect du module sqlite3,
 puis on exécute une requête SQL pour sélectionner tous les utilis
"""

