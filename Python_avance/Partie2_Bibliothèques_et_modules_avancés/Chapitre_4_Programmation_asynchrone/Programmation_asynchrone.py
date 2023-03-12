"""
La programmation asynchrone est un modèle de programmation qui permet d'exécuter des tâches de manière concurrente sans bloquer le thread principal. En Python, la programmation asynchrone est mise en œuvre à l'aide de la bibliothèque asyncio, qui fournit une manière élégante et efficace de gérer les entrées/sorties bloquantes.

Dans ce chapitre, nous commençons par expliquer le fonctionnement de la programmation asynchrone en Python, en montrant comment les coroutines et les événements sont utilisés pour gérer les entrées/sorties de manière efficace. Nous abordons également l'utilisation de la bibliothèque asyncio pour créer des tâches asynchrones et les exécuter en parallèle.

Nous montrons également comment la programmation asynchrone peut améliorer les performances d'une application en réduisant le temps d'attente et en utilisant efficacement les ressources de l'ordinateur. Nous explorons également les avantages de la programmation asynchrone en matière de scalabilité, de modularité et de maintenabilité du code.
"""

# Fonctionnement de la programmation asynchrone

"""
En Python, la programmation asynchrone est basée sur les coroutines et les événements. Les coroutines sont des fonctions spéciales qui peuvent être suspendues et reprises plus tard, ce qui permet d'exécuter plusieurs tâches de manière concurrente. Les événements sont des signaux qui indiquent que quelque chose s'est produit, comme une requête réseau qui a été reçue ou une donnée qui est disponible.

La bibliothèque asyncio fournit une manière élégante et efficace de gérer les coroutines et les événements en Python. Elle utilise un boucle d'événements (event loop) pour exécuter les coroutines de manière concurrente, en attendant les événements et en les traitant au fur et à mesure qu'ils se produisent.

Voici un exemple de coroutine qui effectue une requête réseau :
"""

import asyncio
import aiohttp

async def get_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

loop = asyncio.get_event_loop()
result = loop.run_until_complete(get_url("https://www.google.com"))
print(result)


"""
Dans cet exemple, la coroutine "get_url" utilise la bibliothèque aiohttp pour effectuer une requête réseau asynchrone et renvoyer le résultat.
 La boucle d'événements est exécutée à l'aide de la méthode "run_until_complete" de l'objet loop.
"""

# Utilisation de la bibliothèque asyncio

"""
La bibliothèque asyncio fournit de nombreuses fonctionnalités pour créer et exécuter des coroutines de manière concurrente.
 On peut utiliser la fonction "asyncio.gather" pour exécuter plusieurs coroutines en parallèle et attendre leur résultat. On peut également utiliser les futures asyncio pour effectuer des opérations asynchrones de manière séquentielle.

Voici un exemple de programme qui utilise asyncio pour effectuer plusieurs tâches asynchrones en parallèle :
"""

import asyncio

async def task1():
    await asyncio.sleep(1)
    return "Task 1"

async def task2():
    await asyncio.sleep(1)


# Chapitre 4 : Programmation asynchrone

"""
La programmation asynchrone est une technique avancée de programmation qui permet de gérer de manière efficace les tâches d'attente, telles que les E/S sur disque ou sur réseau. La programmation asynchrone permet de rendre les applications plus réactives et plus performantes,
 car elle permet d'effectuer plusieurs tâches en parallèle sans bloquer le thread principal.

Dans ce chapitre, nous commençons par expliquer le fonctionnement de la programmation asynchrone en Python,
 en montrant comment elle utilise des coroutines et des événements pour gérer les tâches d'attente de manière efficace.
  Nous abordons ensuite l'utilisation de la bibliothèque asyncio, qui est la bibliothèque standard de Python
   pour la programmation asynchrone.

Nous montrons comment utiliser les coroutines pour définir des tâches asynchrones, et comment utiliser
 les événements pour gérer la communication entre les coroutines.
  Nous expliquons également comment utiliser la boucle d'événements d'asyncio pour exécuter les coroutines
   de manière concurrente.

Enfin, nous abordons les avantages de la programmation asynchrone en matière de performance, 
de réactivité et de maintenabilité du code. Nous montrons comment
 la programmation asynchrone peut améliorer considérablement les performances 
 d'une application en permettant de gérer efficacement les tâches d'attente, 
 et comment elle peut rendre l'application plus réactive en évitant les blocages inutiles. 
 Nous montrons également comment la programmation asynchrone peut 
rendre le code plus facile à lire et à maintenir en évitant les constructions complexes telles que les callbacks imbriqués.
"""

# Fonctionnement de la programmation asynchrone


"""
En Python, la programmation asynchrone utilise des coroutines pour définir des tâches asynchrones. 
Une coroutine est une fonction qui peut être interrompue à tout moment pour permettre l'exécution d'autres tâches, puis reprise plus tard avec l'état sauvegardé.

La programmation asynchrone utilise également des événements pour gérer la communication entre les coroutines.
 Un événement est un objet qui permet de signaler la disponibilité d'une ressource ou la survenue d'un événement, afin que les coroutines puissent être notifiées et réveillées.

La bibliothèque asyncio de Python fournit des outils pour gérer efficacement les coroutines et les événements, en utilisant une boucle d'événements pour exécuter les tâches asynchrones de manière concurrente.

Voici un exemple simple de coroutine qui attend une durée donnée avant de renvoyer un résultat :
"""

import asyncio

async def wait_and_return(delay, value):
    await asyncio.sleep(delay)
    return value

async def main():
    coroutines = [wait_and_return(2, "hello"), wait_and_return(1, "world")]
    results = await asyncio.gather(*coroutines)
    print(results)

asyncio.run(main())



# Chapitre 4 : Programmation asynchrone

"""
La programmation asynchrone est une technique avancée de programmation qui permet d'exécuter des tâches en parallèle, sans bloquer le programme principal. Python offre un support complet de la programmation asynchrone grâce à la bibliothèque asyncio, qui permet d'écrire des programmes asynchrones de manière élégante et efficace.

Dans ce chapitre, nous commençons par expliquer le fonctionnement de la programmation asynchrone en Python,
 en montrant comment utiliser la bibliothèque asyncio pour exécuter des tâches en parallèle. Nous abordons ensuite les coroutines, qui sont des fonctions asynchrones spéciales qui permettent de créer des tâches asynchrones.

Nous explorons également les avantages de la programmation asynchrone en matière de performance et d'évolutivité.
 Nous montrons comment la programmation asynchrone peut être utilisée pour exécuter des tâches simultanément 
 sans bloquer le programme principal, et comment elle peut améliorer les performances et l'évolutivité des applications.

Enfin, nous abordons les limites de la programmation asynchrone, en montrant comment 
elle peut être complexe à mettre en place et à déboguer, et comment elle peut ne pas convenir à 
tous les types d'applications.
"""

# Fonctionnement de la programmation asynchrone


"""
En Python, la programmation asynchrone est basée sur des tâches asynchrones, 
qui peuvent être exécutées simultanément sans bloquer le programme principal.
 Les tâches asynchrones sont gérées par la bibliothèque asyncio, qui permet de créer des coroutines asynchrones spéciales.

Les coroutines sont des fonctions asynchrones qui peuvent être interrompues et reprises à tout moment,
 ce qui permet d'exécuter des tâches asynchrones sans bloquer le programme principal.
  Les coroutines sont définies en utilisant le mot-clé "async def", et peuvent être 
  appelées de manière asynchrone en utilisant l'instruction "await".

Voici un exemple de coroutine qui effectue une tâche asynchrone :
"""

import asyncio

async def task():
    print("Début de la tâche...")
    await asyncio.sleep(2)
    print("Fin de la tâche !")

asyncio.run(task())


"""
Dans cet exemple, la coroutine "task" effectue une tâche asynchrone qui consiste à attendre 2 secondes avant d'afficher un message. 
La coroutine est appelée de manière asynchrone en utilisant la fonction "asyncio.run".
"""

# Utilisation de la bibliothèque asyncio

"""
La bibliothèque asyncio offre de nombreux outils pour gérer les tâches asynchrones en Python.
 On peut créer des tâches asynchrones en utilisant des coroutines, et les exécuter simultanément en utilisant la fonction "asyncio.gather". On peut également créer des boucles d'événements asynchrones pour gérer des événements entrants, comme des connexions réseau ou des entrées utilisateur.

Voici un exemple qui illustre l'utilisation de la bibliothèque asyncio pour exécuter des tâches asynchrones :
"""
import asyncio

async def task1():
    print("Début de la tâche 1...")


# Chapitre 4 : Programmation asynchrone

"""
La programmation asynchrone est une technique avancée de programmation qui permet de gérer efficacement des tâches simultanées dans un programme. En Python, la programmation asynchrone est supportée par la bibliothèque standard asyncio, qui permet de gérer des coroutines, des tâches asynchrones et des événements.

Dans ce chapitre, nous commençons par expliquer le fonctionnement de la programmation asynchrone en Python, en montrant comment elle peut être utilisée pour gérer des tâches simultanées de manière efficace et élégante. Nous abordons ensuite la création de coroutines, qui permettent d'exécuter des tâches asynchrones de manière efficace.

Nous explorons également les avantages de la programmation asynchrone en matière de performance, d'évolutivité et de maintenabilité du code. 
Nous montrons comment la programmation asynchrone peut être utilisée pour améliorer la vitesse et l'efficacité des programmes, et comment elle peut faciliter la gestion des tâches simultanées dans une application.
"""

# Fonctionnement de la programmation asynchrone

"""
En Python, la programmation asynchrone est basée sur la notion de coroutines. Les coroutines sont des fonctions qui peuvent être exécutées de manière asynchrone, c'est-à-dire qu'elles peuvent être interrompues à tout moment pour laisser la place à une autre tâche.

La bibliothèque asyncio fournit un mécanisme pour gérer les coroutines, en utilisant le concept de boucle d'événements.
 La boucle d'événements permet de gérer les tâches asynchrones en temps réel, en les exécutant dans un ordre spécifique et en s'assurant que chaque tâche a suffisamment de temps CPU pour s'exécuter.

Voici un exemple de coroutine qui calcule la somme des nombres de 1 à n :
"""

import asyncio

async def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
        await asyncio.sleep(0)
    return total

async def main():
    tasks = [sum_n(10**6), sum_n(10**6+1), sum_n(10**6+2)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())


"""
Dans cet exemple, la fonction "sum_n" est une coroutine qui calcule la somme des nombres de 1 à n. La fonction "main" crée trois tâches asynchrones en utilisant la fonction "asyncio.gather", qui permet d'exécuter plusieurs coroutines en parallèle. 
Les résultats de toutes les tâches sont retournés en utilisant la fonction "await asyncio.gather(*tasks)".
"""

# Utilisation de la bibliothèque asyncio

"""
La bibliothèque asyncio fournit de nombreux outils pour gérer les tâches asynchrones en Python. Voici quelques-uns des outils les plus couramment utilisés :

"async with" : permet d'utiliser des ressources asynchrones de manière élégante, en garantissant que les ressources sont correctement libérées même en cas d'erreur.

"async for" : permet de parcourir des itérables de manière
"""

# Chapitre 4 : Programmation asynchrone

"""
La programmation asynchrone est une technique de programmation qui permet à un programme de traiter
 plusieurs tâches en même temps, sans avoir à attendre la fin de chaque tâche avant de passer à la suivante.
  En Python, la programmation asynchrone est implémentée à l'aide de la bibliothèque asyncio.

Dans ce chapitre, nous commençons par expliquer le fonctionnement de la programmation asynchrone en Python,
 en montrant comment utiliser les coroutines pour gérer les tâches asynchrones.
 Nous abordons ensuite l'utilisation de la boucle d'événements asyncio, qui permet de planifier et d'exécuter 
 les coroutines de manière efficace.

Nous montrons également comment utiliser les tâches et les futurs asyncio pour gérer les résultats des coroutines, 
ainsi que les verrous et les sémaphores asyncio pour gérer l'accès concurrent aux ressources partagées.

Enfin, nous abordons les avantages de la programmation asynchrone en matière de performance et d'évolutivité,
 et comment elle peut être utilisée pour créer des applications rapides, réactives et évolutives.
"""

# Fonctionnement de la programmation asynchrone en Python

"""
En Python, la programmation asynchrone est implémentée à l'aide de la bibliothèque asyncio,
 qui fournit des primitives pour gérer les tâches asynchrones. 
Les coroutines asyncio sont des fonctions qui peuvent être interrompues et reprises à tout moment,
 permettant ainsi à un programme de traiter plusieurs tâches en même temps.

La boucle d'événements asyncio est un objet qui gère la planification et l'exécution des coroutines.
 La boucle d'événements récupère les coroutines prêtes à être exécutées, les exécute, puis passe à la coroutine suivante.
"""

import asyncio

async def coroutine():
    print("Début de la coroutine")
    await asyncio.sleep(1)
    print("Fin de la coroutine")

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine())


"""
Dans cet exemple, la coroutine "coroutine" utilise la fonction "asyncio.sleep" pour simuler une tâche asynchrone.
 La boucle d'événements récupère la coroutine, l'exécute, puis passe à la coroutine suivante.
"""
# Tâches et futurs asyncio

"""
Les tâches asyncio sont des objets qui permettent de gérer l'exécution des coroutines de manière asynchrone. Les tâches sont créées à partir de coroutines en utilisant la fonction "asyncio.create_task", et peuvent être utilisées pour attendre la fin de l'exécution d'une coroutine.

Les futurs asyncio sont des objets qui représentent les résultats d'une tâche asynchrone. Les futurs sont créés à partir de tâches en utilisant la méthode "task.get_future", et peuvent être utilisés pour attendre la fin de l'exécution d'une tâche.

Voici un exemple qui illustre l'utilisation des tâches et des futurs asyncio :
"""

import asyncio

async def coroutine():
    await asyncio.sleep(1)
    return 42

async def main():
    task = asyncio.create_task(coroutine())
    print("Tâche créée")
    result = await task
    print("R")



# Chapitre 4 : Programmation asynchrone

"""
La programmation asynchrone est un paradigme de programmation qui permet de gérer efficacement des tâches simultanées dans un programme. Python offre une bibliothèque standard pour la programmation asynchrone,
 asyncio, qui permet de gérer des opérations d'entrée/sortie non bloquantes de manière élégante et efficace.

Dans ce chapitre, nous commençons par expliquer le fonctionnement de la programmation asynchrone en Python,
 en montrant comment les fonctions asynchrones peuvent être utilisées pour gérer des tâches simultanées.
  Nous abordons ensuite les coroutines, qui sont des fonctions asynchrones qui permettent de gérer 
  des opérations d'entrée/sortie non bloquantes.

Nous montrons comment utiliser la bibliothèque asyncio pour gérer des tâches simultanées,
 en utilisant des coroutines, des tâches et des événements. Nous explorons également les avantages de la programmation asynchrone en matière de performance, d'évolutivité et de maintenabilité du code.
"""


# Fonctionnement de la programmation asynchrone

"""
La programmation asynchrone en Python repose sur les fonctions asynchrones et les coroutines.
 Les fonctions asynchrones sont des fonctions qui peuvent être interrompues et reprises à tout moment,
  ce qui permet de gérer des tâches simultanées sans bloquer le programme.

Les coroutines sont des fonctions asynchrones qui permettent de gérer des opérations d'entrée/sortie non bloquantes. 
Une coroutine peut être mise en pause lorsqu'elle rencontre une opération d'entrée/sortie, et 
reprise plus tard lorsque l'opération est terminée.

Voici un exemple de coroutine qui effectue une opération d'entrée/sortie non bloquante :
"""
import asyncio

async def lire_fichier(nom_fichier):
    with open(nom_fichier, "r") as f:
        contenu = await f.read()
    return contenu

loop = asyncio.get_event_loop()
resultat = loop.run_until_complete(lire_fichier("mon_fichier.txt"))
print(resultat)


"""
Dans cet exemple, la coroutine "lire_fichier" ouvre un fichier en mode lecture,
 lit son contenu de manière asynchrone et renvoie le contenu.
 La boucle d'événements asyncio est utilisée pour exécuter la coroutine et attendre le résultat.
"""

# Utilisation de la bibliothèque asyncio

"""
La bibliothèque asyncio offre des fonctionnalités avancées pour gérer des tâches simultanées en Python. 
On peut créer des coroutines, des tâches et des événements, qui permettent de gérer des opérations asynchrones
 de manière élégante et efficace.

Voici un exemple de programme qui utilise asyncio pour gérer des tâches simultanées :
"""

import asyncio

async def task(n):
    await asyncio.sleep(1)
    print("Tâche", n, "terminée")

async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())
