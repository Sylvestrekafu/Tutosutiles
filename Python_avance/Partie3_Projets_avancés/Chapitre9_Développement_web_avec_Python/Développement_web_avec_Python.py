"""
ython est un langage de programmation populaire pour le développement web,
grâce à sa simplicité, sa flexibilité et sa richesse en bibliothèques.
 Python offre une gamme de frameworks et de bibliothèques pour le développement web,
 qui permettent de créer des applications web sophistiquées et de haute qualité.

Dans ce chapitre, nous abordons le développement web avec Python,
en montrant comment créer des applications web avec les frameworks Flask et Django.
 Nous expliquons également les différents concepts du développement web,
 comme les templates, les routes et les vues, et comment les mettre en œuvre en Python.

Nous montrons également comment utiliser les bibliothèques Python pour l'interrogation
 de bases de données et le traitement de données, qui sont des tâches courantes dans le développement web.

Enfin, nous explorons les avantages du développement web avec Python,
en termes de rapidité de développement, de flexibilité et de sécurité.
Nous montrons comment les frameworks et les bibliothèques Python peuvent aider à créer des
 applications web de manière efficace et rapide, tout en garantissant la sécurité et la fiabilité.
"""

# Frameworks Flask et Django

"""
Les frameworks Flask et Django sont les deux frameworks les plus populaires pour le développement web en Python.
 Flask est un framework minimaliste et flexible, qui permet de créer des applications web légères et simples.
  Django est un framework plus complet et structuré, qui fournit une gamme de fonctionnalités avancées pour
   le développement web.

Voici un exemple de création d'une application web simple avec Flask :
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    return "Bonjour, monde !"

@app.route('/presentation/<nom>')
def presentation(nom):
    return render_template("presentation.html", nom=nom)

if __name__ == '__main__':
    app.run()


# Dans cet exemple, on crée une application web simple avec Flask, qui a deux routes :
# la route '/' affiche un message de bienvenue, et la route '/presentation/nom'
# affiche une page HTML de présentation avec le nom de l'utilisateur.

# Interrogation de bases de données

"""
L'interrogation de bases de données est une tâche courante dans le développement web,
 qui consiste à récupérer des données stockées dans une base de données. 
 Python offre une gamme de bibliothèques pour l'interrogation de bases de données, comme SQLAlchemy et Django ORM.

Voici un exemple d'interrogation d'une base de données SQLite avec SQLAlchemy :
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    age = Column(Integer)
    ville = Column(String)

moteur = create_engine('sqlite:///ma_base_de_donnees.db')
Base.metadata.create_all(moteur)

Session = sessionmaker(bind=moteur)
session = Session()

utilisateurs = session.query(Utilisateur).all()
for utilisateur in utilisateurs:
    print(utilisateur.nom, utilisateur.age, utilisateur.ville)


# Dans cet exemple, on crée une base de données SQLite avec SQLAlchemy,
# en définissant une classe Utilisateur qui correspond à une table de la base de données.
# On crée ensuite une session SQLAlchemy pour interroger la base de

# Chapitre 9 : Développement web avec Python

"""
Python est un langage de programmation polyvalent qui peut être utilisé pour le développement web.
 Python offre une variété de frameworks et d'outils pour le développement web,
  qui permettent de créer des applications web sophistiquées et sécurisées.

Dans ce chapitre, nous commençons par expliquer les principaux concepts du développement web,
 comme les protocoles HTTP et les technologies front-end et back-end. Nous montrons 
 comment Python peut être utilisé pour créer des applications web, en utilisant des frameworks comme Flask et Django.

Nous abordons également la création de bases de données pour les applications web,
 en montrant comment utiliser des outils comme SQLAlchemy et Django ORM pour 
 interagir avec des bases de données relationnelles.

Enfin, nous explorons les avantages du développement web avec Python en matière de sécurité,
 de performances et de productivité. Nous montrons comment les frameworks et les outils de
  la bibliothèque standard peuvent être utilisés pour créer des applications web de manière efficace et sécurisée, 
et comment ils peuvent améliorer la qualité et la maintenance du code.
"""

# Concepts de développement web

"""
Le développement web implique la création d'applications qui sont accessibles via Internet ou un intranet.
 Les principales technologies du développement web sont les protocoles HTTP, qui permettent 
 la communication entre les clients et les serveurs, et les technologies front-end et back-end,
  qui permettent de créer des interfaces utilisateur et des services web.

Voici un exemple de création d'une application web en utilisant le framework Flask :
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Bonjour, monde !"

if __name__ == "__main__":
    app.run()


"""
Dans cet exemple, on crée une application web en utilisant le framework Flask. 
On définit une route "/", qui affiche le message "Bonjour, monde !" lorsqu'elle est appelée.
 On lance ensuite l'application en utilisant la fonction run().
"""

# Bases de données pour les applications web

# Les applications web nécessitent souvent l'utilisation de bases de données pour stocker
# des informations de manière persistante. Python offre des outils comme SQLAlchemy et
# Django ORM pour interagir avec des bases de données relationnelles.
#
# Voici un exemple d'utilisation de SQLAlchemy pour interagir avec une base de données SQLite :

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Personne(Base):
    __tablename__ = "personnes"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    age = Column(Integer)

moteur = create_engine("sqlite:///ma_base_de_donnees.db")
Session = sessionmaker(bind=moteur)
session = Session()

Base.metadata.create_all(moteur)

p1 = Personne(nom="Alice", age=30)
session.add(p1)
session.commit()

personnes = session.query(Personne).all()
for personne in personnes:
    print(personne.nom, personne.age)


"""
Dans cet exemple, on crée une classe Personne qui représente une table dans une base de données SQLite.
 On crée ensuite un moteur SQLAlchemy pour se connecter à la base de données, et 
 on crée une session pour interagir avec la base de données. On ajoute ensuite une personne à la base de données, 
on commit les changements, et on affiche les personnes dans la base de données.
"""

# Chapitre 9 : Tests et débogage


"""
Les tests et le débogage sont des aspects importants de la programmation, 
qui permettent de s'assurer que le code fonctionne correctement et de corriger
 les erreurs et les bugs. Python offre une bibliothèque standard complète pour 
 les tests et le débogage, qui permet de créer des tests unitaires, 
des tests d'intégration et des tests de validation, ainsi que de déboguer le code
 à l'aide de messages d'erreur, de tracebacks et de débogueurs interactifs.

Dans ce chapitre, nous abordons les différentes techniques de test et de débogage en Python, 
en montrant comment utiliser les modules de la bibliothèque standard pour créer des tests automatisés,
 des tests interactifs et des messages d'erreur personnalisés.

Nous montrons également comment utiliser les débogueurs interactifs en Python, comme pdb et ipdb,
 pour suivre l'exécution du code pas à pas et identifier les erreurs et les bugs.

Enfin, nous explorons les avantages des tests et du débogage en matière de qualité du code,
 de maintenance et de réduction des coûts. Nous montrons comment les tests et le débogage peuvent aider 
 à améliorer la qualité du code, à faciliter la maintenance et l'évolution du code à long terme, et à réduire les coûts de développement et de maintenance.
"""

# Tests automatisés

"""
Les tests automatisés sont une technique de test courante en Python, 
qui consiste à écrire des tests qui vérifient le bon fonctionnement du code de manière automatique. 
Python offre un module de tests unitaires complet, unittest, 
qui permet de créer des tests automatisés pour des fonctions et des classes Python.

Voici un exemple de création d'un test unitaire en Python, en utilisant le module unittest de la bibliothèque standard :
"""

import unittest

def addition(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

"""
Dans cet exemple, on définit une fonction addition qui ajoute deux nombres, 
et on crée un test unitaire avec la classe TestAddition du module unittest.
 On teste ensuite la fonction addition en utilisant la méthode assertEqual de la classe TestCase, 
qui vérifie que le résultat de la fonction est égal à une valeur donnée.
"""

# Débogage interactif


"""
Le débogage interactif est une technique de débogage courante en Python, 
qui consiste à suivre l'exécution du code pas à pas et à identifier les erreurs et 
les bugs à l'aide de messages d'erreur, de tracebacks et de débogueurs interactifs.

Python offre deux débogueurs interactifs populaires, pdb et ipdb, qui permettent de 
suivre l'exécution du code pas à pas, d'inspecter les variables et les expressions, 
et de modifier le code en temps réel.

Voici un exemple d'utilisation du débogueur pdb en Python, pour déboguer une 
fonction qui calcule la somme des éléments d'une liste :
"""

import pdb

def somme_liste(liste):
    somme = 0


# Chapitre 9 : Développement web avec Python

"""
Le développement web est un domaine important de la programmation,
 qui consiste à créer des sites web et des applications web pour le World Wide Web. 
 Python offre une variété de bibliothèques et de frameworks pour le développement web, 
qui permettent de créer des sites web et des applications web dynamiques et interactives.

Dans ce chapitre, nous commençons par expliquer les différents composants d'une application web, 
comme le serveur web, le client web, le protocole HTTP et les langages de programmation web.
 Nous montrons comment utiliser les modules de la bibliothèque standard pour créer des serveurs web en Python, 
 en utilisant les protocoles HTTP et WebSocket.

Nous abordons également les frameworks web populaires en Python, comme Flask et Django.
 Nous montrons comment utiliser ces frameworks pour créer des applications web sophistiquées,
  en utilisant des modèles, des vues et des contrôleurs.

Enfin, nous explorons les avantages du développement web en Python en matière de productivité, 
de sécurité et de maintenabilité. Nous montrons comment les bibliothèques et les frameworks 
de développement web en Python peuvent améliorer la qualité et la sécurité des applications web, 
tout en réduisant le temps de développement et de maintenance.
"""

# Création d'un serveur web en Python

"""
La création d'un serveur web en Python est une tâche courante dans le développement web. 
Python offre des fonctionnalités complètes pour la création de serveurs web, 
en utilisant les modules de la bibliothèque standard comme http.server et socketserver.

Voici un exemple de création d'un serveur web en Python,
 en utilisant la classe SimpleHTTPRequestHandler du module http.server :
"""
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serveur démarré sur le port", PORT)
    httpd.serve_forever()



"""
Dans cet exemple, on crée un serveur web en utilisant la classe TCPServer du module socketserver et 
la classe SimpleHTTPRequestHandler du module http.server. On spécifie le port sur lequel le serveur doit écouter,
 et on démarre le serveur en appelant la méthode serve_forever
"""

# Utilisation des frameworks web en Python

"""
Les frameworks web sont des bibliothèques logicielles qui facilitent le développement 
d'applications web en fournissant des fonctionnalités communes comme l'authentification,
 la gestion des sessions et la gestion des formulaires. Flask et Django
  sont des frameworks web populaires en Python, qui permettent de créer
   des applications web sophistiquées avec peu de code.

Voici un exemple de création d'une application web Flask en Python :
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()

# Dans cet exemple, on crée une application web Flask en définissant deux routes,
# accueil et contact, qui renvoient des pages HTML générées à partir de modèles Jinja2.
#
# On démarre ensuite l'application en appelant la méthode run.


# Avantages du développement web en Python
# Le développement web en Python offre de nombreux avantages en termes de productivité, de sécurité et de

# Chapitre 9 : Tests et débogage avancés

"""
Les tests et le débogage sont des tâches essentielles de la programmation,
 qui permettent de s'assurer que le code fonctionne correctement et de corriger les erreurs éventuelles.
  Python offre une bibliothèque standard complète pour les tests et le débogage, qui permet de créer des tests unitaires,
 des tests d'intégration et des tests fonctionnels, ainsi que de déboguer le code en utilisant des outils avancés.

Dans ce chapitre, nous commençons par expliquer les différents types de tests couramment utilisés en Python, 
comme les tests unitaires, les tests d'intégration et les tests fonctionnels. Nous montrons comment utiliser
 les modules de la bibliothèque standard pour créer des tests, et comment les exécuter pour s'assurer que le
  code fonctionne correctement.

Nous abordons également le débogage en Python, en montrant comment utiliser les outils de débogage de 
la bibliothèque standard pour identifier et corriger les erreurs dans le code.

Enfin, nous explorons les avantages des tests et du débogage en matière de qualité du code, 
de fiabilité et de maintenabilité. Nous montrons comment les tests et le débogage peuvent aider
 à réduire les erreurs et les bugs dans le code, et comment ils peuvent faciliter la maintenance et
  l'évolution du code à long terme.
"""

# Tests unitaires, tests d'intégration et tests fonctionnels

"""
Les tests unitaires, les tests d'intégration et les tests fonctionnels sont les types de tests couramment
 utilisés en Python. Les tests unitaires sont utilisés pour tester des parties individuelles du code, 
 comme des fonctions ou des méthodes de classe. Les tests d'intégration sont utilisés pour tester
  la compatibilité et la cohérence des différentes parties du code. Les tests fonctionnels 
  sont utilisés pour tester le comportement global du code, en utilisant des scénarios réels.

Voici un exemple de création d'un test unitaire en Python, en utilisant le module unittest de la bibliothèque standard :
"""

import unittest

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

class TestFactorielle(unittest.TestCase):
    def test_factorielle_0(self):
        self.assertEqual(factorielle(0), 1)

    def test_factorielle_1(self):
        self.assertEqual(factorielle(1), 1)

    def test_factorielle_5(self):
        self.assertEqual(factorielle(5), 120)

if __name__ == '__main__':
    unittest.main()

"""
Dans cet exemple, on crée une fonction factorielle qui calcule la factorielle d'un nombre entier,
 et on crée une classe TestFactorielle qui contient trois tests unitaires pour cette fonction.
 On utilise la méthode assertEqual pour s'assurer que le résultat de chaque test est égal au résultat attendu.
"""

# Débogage

"""
Le débogage est une tâche essentielle de la programmation, qui permet de trouver et de corriger les erreurs dans le code. 
Python offre des outils avancés pour le débogage, comme la fonction print, le module pdb, et les IDE intégrés.
"""
