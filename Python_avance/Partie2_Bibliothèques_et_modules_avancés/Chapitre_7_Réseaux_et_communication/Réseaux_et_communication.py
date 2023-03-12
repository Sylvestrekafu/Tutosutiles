"""
La communication entre ordinateurs est une tâche courante de la programmation,
qui consiste à envoyer et recevoir des données entre des ordinateurs connectés à un réseau.
Python offre une bibliothèque standard complète pour la communication réseau,
qui permet de créer des connexions TCP/IP, d'envoyer et de recevoir des données, et d'interagir avec des serveurs web.

Dans ce chapitre, nous commençons par expliquer les principes de base de la communication réseau,
en montrant comment les ordinateurs communiquent en utilisant le protocole TCP/IP.
Nous abordons ensuite la création de connexions réseau en Python, en montrant comment créer
 des sockets TCP/IP et se connecter à des serveurs.

Nous explorons également la communication réseau en Python, en montrant comment envoyer et
 recevoir des données en utilisant des sockets, et comment interagir avec des serveurs web en utilisant des requêtes HTTP.

Enfin, nous explorons les avantages de la communication réseau en matière de développement
d'applications distribuées, de services web et de systèmes distribués.
Nous montrons comment les fonctionnalités de la bibliothèque standard
de Python peuvent être utilisées pour créer des applications distribuées efficaces et évolutives.
"""

# Principes de la communication réseau

"""
La communication réseau en Python repose sur le protocole TCP/IP, 
qui permet à des ordinateurs de communiquer en utilisant des sockets TCP/IP. Les sockets sont des objets qui permettent de créer des connexions réseau et d'envoyer et de recevoir des données.

Voici un exemple de création d'une socket TCP/IP en Python :
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.google.com", 80))
s.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
response = s.recv(4096)
print(response)
s.close()


"""
Dans cet exemple, on crée une socket TCP/IP en utilisant la fonction socket du module socket,
 puis on se connecte à un serveur en utilisant la fonction connect.
  On envoie ensuite une requête HTTP en utilisant la méthode send, 
  et on reçoit la réponse du serveur en utilisant la méthode recv.
"""

# Communication réseau en Python

"""
La bibliothèque standard de Python offre des fonctionnalités complètes pour la communication réseau, 
en permettant de créer des sockets TCP/IP, d'envoyer et de recevoir des données, et d'interagir avec des serveurs web.

Voici un exemple de création d'un serveur TCP/IP en Python :
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8080))
s.listen(5)

while True:
    client, adresse = s.accept()
    data = client.recv(4096)
    response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, world!"
    client.send(response)
    client.close()


"""
Dans cet exemple, on crée un serveur TCP/IP en utilisant la fonction socket du module socket, 
puis on écoute les connexions entrantes en utilisant la méthode listen. Lorsqu'une connexion est établie, on accepte la connexion en utilisant la méthode accept, 
puis on reçoit les données du client en utilisant la méthode recv. On envoie ensuite une réponse au
"""


# Chapitre 7 : Réseaux et communication

"""
Les réseaux et la communication sont des aspects clés de la programmation moderne, 
qui permettent aux applications de communiquer avec d'autres applications, 
de transférer des données sur le réseau et de fournir des services à distance. 
Python offre une bibliothèque standard pour la communication réseau, qui permet 
de créer des applications réseau et des protocoles de communication de manière élégante et efficace.

Dans ce chapitre, nous commençons par expliquer les principes de base de la communication réseau
 en Python, en montrant comment les sockets peuvent être utilisés pour créer des connexions réseau et 
 échanger des données. Nous abordons ensuite les protocoles de communication couramment utilisés en Python,
  comme HTTP, FTP, SMTP et POP3, en montrant comment interagir avec ces protocoles à l'aide des modules de 
  la bibliothèque standard.

Nous explorons également les avantages de la communication réseau en matière de portabilité,
 d'interopérabilité et de scalabilité, en montrant comment les applications réseau peuvent être 
 conçues pour fonctionner sur différents systèmes d'exploitation, architectures et protocoles.
"""

# Principes de base de la communication réseau

"""
La communication réseau en Python repose sur les sockets, qui sont des interfaces de programmation de bas niveau pour 
les connexions réseau. Les sockets permettent de créer des connexions réseau entre des applications, 
d'envoyer et de recevoir des données sur le réseau, et de gérer des protocoles de communication complexes.

Voici un exemple de création d'un serveur TCP qui écoute sur le port 1234 :
"""

import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("localhost", 1234))
serveur.listen(1)
connexion, adresse = serveur.accept()
donnees = connexion.recv(1024)
connexion.sendall(b"Message reçu : " + donnees)
connexion.close()

# Dans cet exemple, on crée un socket serveur qui écoute sur le port 1234.
# On accepte ensuite une connexion entrante, on reçoit des données du client et on renvoie une réponse.

# Protocoles de communication couramment utilisés

"""
Python offre des modules pour interagir avec différents protocoles de communication couramment utilisés,
 comme HTTP, FTP, SMTP et POP3. Ces modules permettent d'envoyer et de recevoir des données sur le réseau en utilisant des protocoles standardisés.

Voici un exemple d'envoi d'un courriel en utilisant le protocole SMTP :
"""

import smtplib

serveur_smtp = "smtp.example.com"
port_smtp = 587
utilisateur_smtp = "mon_nom_utilisateur"
mot_de_passe_smtp = "mon_mot_de_passe"

connexion_smtp = smtplib.SMTP(serveur_smtp, port_smtp)
connexion_smtp.starttls()
connexion_smtp.login(utilisateur_smtp, mot_de_passe_smtp)
message = "De: moi@example.com\nÀ: toi@example.com\nSujet: Hello\n\nHello, world!"
connexion_smtp.sendmail("moi@example.com", "toi@example.com", message)
connexion_smtp.quit()


"""
Dans cet exemple, on se connecte à un serveur SMTP en utilisant la classe SMTP du module smtplib, 
on s'authentifie avec un nom d'utilisateur et un mot de passe, on crée un message et on envoie le message.

Avantages de la communication réseau
"""


# Chapitre 7 : Réseaux et communication

"""
La communication entre les ordinateurs est une tâche essentielle de la programmation,
 qui permet de connecter des applications et des services à travers Internet. 
 Python offre une bibliothèque standard complète pour la communication réseau,
  qui permet de créer des serveurs, des clients et des protocoles réseau de manière élégante et efficace.

Dans ce chapitre, nous commençons par expliquer les concepts de base de la communication réseau,
 comme les protocoles, les adresses IP et les ports. 
 Nous abordons ensuite l'utilisation de la bibliothèque socket de la bibliothèque standard, 
 qui permet de créer des connexions TCP et UDP, d'envoyer et de recevoir des données, 
 et de gérer des connexions en mode serveur et en mode client.

Nous montrons également l'utilisation de la bibliothèque requests, qui permet de réaliser 
des requêtes HTTP et de récupérer des données à partir de serveurs web.
 Enfin, nous explorons les avantages de la communication réseau en matière d'intégration de services, 
 de partage de données et de sécurité. Nous montrons comment les outils de la bibliothèque 
standard peuvent être utilisés pour connecter des applications à travers Internet de manière robuste et sécurisée.
"""

# Concepts de base de la communication réseau

"""
La communication réseau repose sur des concepts de base tels que les protocoles, 
les adresses IP et les ports. Les protocoles sont des ensembles de règles et 
de conventions qui définissent le format et le contenu des messages échangés
 entre les ordinateurs. Les adresses IP sont des identifiants uniques qui 
 permettent de localiser les ordinateurs sur Internet. 
Les ports sont des numéros de canal qui permettent de distinguer différents services sur un même ordinateur.
"""

# Utilisation de la bibliothèque socket

"""
La bibliothèque socket de la bibliothèque standard de Python permet de créer des connexions réseau,
 d'envoyer et de recevoir des données, et de gérer des connexions en mode serveur et en mode client.
  On peut créer des connexions TCP et UDP en utilisant la fonction socket, et on peut envoyer
   et recevoir des données en utilisant les méthodes send et recv.

Voici un exemple de création d'un serveur TCP qui écoute sur le port 1234 et qui renvoie 
la chaîne de caractères "Hello, world !" à chaque client qui se connecte :
"""

import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("localhost", 1234))
serveur.listen()

while True:
    client, adresse = serveur.accept()
    print("Connexion de", adresse)
    client.send(b"Hello, world !")
    client.close()


"""
Dans cet exemple, on crée un serveur TCP qui écoute sur l'adresse localhost et le port 1234. On utilise la méthode listen pour écouter les connexions entrantes. On boucle ensuite sur les connexions entrantes, en utilisant la méthode accept pour accepter les connexions. On envoie ensuite la chaîne de caractères "Hello, world !" au client, 
en utilisant la méthode send. Enfin, on ferme la connexion cliente avec la méthode close.
"""

# Utilisation de la bibliothèque requests
# La bibliothèque requests permet de réaliser des requêtes HTTP et de récupérer des données à partir de serveurs web.


# Chapitre 7 : Réseaux et communication

"""
La communication en réseau est une tâche courante de la programmation,
 qui consiste à échanger des données entre des ordinateurs connectés en réseau. 
Python offre une bibliothèque standard pour la communication en réseau,
 qui permet de créer des applications de réseau complexes en utilisant des protocoles comme TCP/IP, UDP et HTTP.

Dans ce chapitre, nous commençons par expliquer les principes de la communication en réseau,
 en montrant comment les protocoles TCP/IP, UDP et HTTP sont utilisés pour échanger des données en réseau.

Nous abordons ensuite la création de serveurs et de clients en réseau en Python, 
en montrant comment utiliser les modules socket, asyncio et http.server pour créer des applications de réseau.

Enfin, nous explorons les avantages de la communication en réseau en matière de collaboration,
 de partage de données et d'interopérabilité. Nous montrons comment les applications de réseau peuvent être utilisées pour partager des données entre des ordinateurs, pour collaborer à distance et pour fournir des services à des utilisateurs distants.
"""

# Principes de la communication en réseau

"""
La communication en réseau repose sur des protocoles de communication comme TCP/IP, UDP et HTTP. 
Le protocole TCP/IP est utilisé pour établir des connexions fiables entre des ordinateurs connectés en réseau,
 tandis que le protocole UDP est utilisé pour des échanges de données moins fiables mais plus rapides.
  Le protocole HTTP est utilisé pour l'échange de données sur le Web.

Les serveurs et les clients en réseau communiquent en utilisant des sockets,
 qui sont des objets qui représentent des connexions de réseau. Les serveurs écoutent sur 
 des ports spécifiques pour les connexions entrantes, tandis que les clients se connectent 
 aux serveurs en spécifiant l'adresse IP et le port du serveur.
"""

# Création de serveurs et de clients en réseau

"""
Python offre des modules pour la création de serveurs et de clients en réseau en utilisant
 les protocoles TCP/IP, UDP et HTTP. Le module socket permet de créer des sockets pour les connexions réseau,
  tandis que le module http.server permet de créer des serveurs Web.

Voici un exemple de création d'un serveur TCP/IP en Python 
"""
import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("localhost", 8080))
serveur.listen(5)
print("Serveur en écoute sur le port 8080...")

while True:
    client, adresse = serveur.accept()
    print("Connexion entrante de :", adresse)
    client.sendall(b"Bonjour, client !")
    client.close()


"""
Dans cet exemple, on crée un serveur TCP/IP en utilisant la fonction socket du module socket.
 On associe le serveur au port 8080, puis on écoute les connexions entrantes. On accepte ensuite 
 une connexion entrante et on envoie un message de bienvenue au client.

Voici un exemple de création d'un client TCP/IP en Python :
"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))
donnees = client.recv(1024)
print(donnees.decode())
client.close()


# Dans cet exemple, on crée un client TCP/IP en utilisant la fonction socket du module socket.
# On se connecte ensuite au serveur en spécifiant l'adresse IP et le port du


# Chapitre 7 : Réseaux et communication

"""
La communication en réseau est un aspect important de la programmation moderne,
 qui permet de connecter des applications à des serveurs distants, 
 d'échanger des données en temps réel et de créer des applications distribuées.
  Python offre une bibliothèque standard complète pour la communication en réseau, 
qui permet de créer des sockets, des clients et des serveurs, et d'interagir 
avec des protocoles de réseau tels que TCP, UDP, HTTP et SMTP.

Dans ce chapitre, nous commençons par expliquer les concepts de base de la communication en réseau,
 en montrant comment les sockets peuvent être utilisés pour établir des connexions réseau et échanger des données.

Nous abordons ensuite l'utilisation de la bibliothèque socket pour créer des clients et des serveurs réseau, 
en montrant comment écouter et accepter des connexions, et comment échanger des données entre les clients et les serveurs.

Nous explorons également les protocoles de réseau couramment utilisés, comme TCP, UDP, HTTP et SMTP,
 en montrant comment utiliser les modules de la bibliothèque standard pour interagir avec ces protocoles.

Enfin, nous explorons les avantages de la communication en réseau en matière de connectivité,
 de scalabilité et de portabilité des applications. Nous montrons comment les applications
  peuvent être développées pour interagir avec des serveurs distants et offrir des fonctionnalités avancées,
   en utilisant les modules de la bibliothèque standard pour la communication en résea
"""

# Les sockets

"""
Les sockets sont une abstraction de la communication en réseau en Python,
 qui permettent d'établir des connexions réseau et d'échanger des données entre les applications.
  Les sockets sont utilisés pour créer des clients et des serveurs réseau,
   qui peuvent échanger des données en temps réel.

Voici un exemple de création d'un socket client en Python :
"""

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8080))
client_socket.send(b"Hello, world!")
reponse = client_socket.recv(1024)
print(reponse)
client_socket.close()


"""
Dans cet exemple, on crée un socket client en utilisant la fonction socket du module socket.
 On se connecte ensuite à un serveur en utilisant la méthode connect du socket client, et on envoie des données en utilisant la méthode send. On reçoit ensuite une réponse du serveur 
en utilisant la méthode recv, et on ferme le socket client.
"""

# Les serveurs

"""
Les serveurs sont des applications qui écoutent des connexions réseau et 
répondent à des demandes de clients. Les serveurs peuvent être créés en utilisant 
la bibliothèque socket et les classes de serveurs définies dans la bibliothèque standard.

Voici un exemple de création d'un serveur TCP en Python :
"""

import socket

serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur_socket.bind(("localhost", 8080))
serveur_socket.listen(1)

while True:
    connexion, adresse = serveur_socket.accept()
    donnees = connexion.recv(1024)
    if donnees:
        reponse = b"Hello, " + donnees
        connexion.send(reponse)
    connexion.close()


# Dans cet exemple, on crée un socket serveur en utilisant la fonction socket du module socket.
# On lie ensuite le socket serveur à une adresse et on le met en écoute en utilisant

# Chapitre 7 : Réseaux et communication

"""
La communication entre ordinateurs est une tâche courante de la programmation, 
qui consiste à échanger des données entre des ordinateurs à travers un réseau. 
Python offre une bibliothèque standard complète pour la communication réseau,
 qui permet de créer des applications réseau sophistiquées.

Dans ce chapitre, nous commençons par expliquer les différents protocoles 
de communication réseau couramment utilisés, comme TCP/IP, HTTP et WebSocket. 
Nous montrons comment utiliser les modules de la bibliothèque standard pour créer 
des clients et des serveurs qui communiquent avec ces protocoles.

Nous abordons également la création de sockets, qui sont des points de terminaison 
de communication dans un réseau. Nous montrons comment créer des sockets en Python, 
et comment les utiliser pour envoyer et recevoir des données.

Enfin, nous explorons les avantages de la communication réseau en matière de traitement de données,
 de collaboration et de portabilité du code. Nous montrons comment les modules de la bibliothèque standard peuvent être utilisés pour créer des applications réseau de manière efficace et portable,
 et comment ils peuvent améliorer la productivité et la qualité du code.
"""

# Protocoles de communication réseau

"""
Les protocoles de communication réseau couramment utilisés en Python sont TCP/IP, HTTP et WebSocket.
 TCP/IP est un protocole de communication fiable, qui garantit que les données sont livrées
  dans l'ordre et sans erreur. HTTP est un protocole de communication sans état, 
  qui est utilisé pour le transfert de documents hypertexte. WebSocket est un protocole de communication bidirectionnel,
   qui permet la communication en temps réel entre un client et un serveur.

Voici un exemple de création d'un client HTTP en Python, en utilisant le module http.client de la bibliothèque standard :
"""
import http.client

connexion = http.client.HTTPSConnection("www.google.com")
connexion.request("GET", "/")
reponse = connexion.getresponse()
print(reponse.status, reponse.reason)
donnees = reponse.read()
print(donnees)

# Dans cet exemple, on crée un client HTTP en utilisant la classe HTTPSConnection du module http.client,
# on envoie une requête GET à l'adresse www.google.com, et on affiche la réponse renvoyée par le serveur.

# Création de sockets

"""
Les sockets sont des points de terminaison de communication dans un réseau. Python offre des fonctionnalités complètes pour créer des sockets en utilisant les modules socket et socketserver de la bibliothèque standard.

Voici un exemple de création d'un serveur TCP en Python, en utilisant le module socketserver de la bibliothèque standard :
"""

import socketserver

class MonGestionnaireDeRequete(socketserver.BaseRequestHandler):
    def handle(self):
        donnees = self.request.recv(1024).strip()
        print("{} a envoyé : {}".format(self.client_address[0], donnees))
        self.request.sendall(donnees.upper())

serveur = socketserver.TCPServer(("localhost", 12345), MonGestionnaireDeRequete)
serveur.serve_forever()


# Dans cet exemple, on crée un serveur TCP en utilisant la classe TCPServer du module socketserver.
# On définit une classe MonGestionnaireDeRequete qui gère les connexions entrantes,
# en lisant les données envoyées par le client, en les affichant et en renvoyant une réponse en majuscules