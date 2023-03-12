"""

Les tests unitaires sont une pratique essentielle de la programmation qui permet de vérifier que
 les fonctions et les méthodes d'un programme fonctionnent correctement. Les tests unitaires consistent à écrire des fonctions de test qui vérifient que les fonctions et les méthodes produisent les résultats attendus
 pour un ensemble de cas de test.

Python offre une bibliothèque standard pour les tests unitaires, unittest, qui permet de définir des cas de test,
 d'exécuter les tests et de vérifier les résultats. Dans ce chapitre, nous commençons par expliquer les principes
  des tests unitaires, en montrant comment écrire des fonctions de test pour vérifier le comportement des fonctions et
   des méthodes.

Nous abordons ensuite l'utilisation de la bibliothèque unittest pour écrire et exécuter des tests unitaires.
Nous montrons comment définir des cas de test, exécuter les tests, vérifier les résultats et générer des rapports de test.

Nous explorons également les avantages des tests unitaires en matière de qualité, de fiabilité et de maintenabilité du code.
 Nous montrons comment les tests unitaires peuvent aider à détecter les erreurs de manière précoce,
 à améliorer la qualité et la robustesse du code, et à faciliter la maintenance du code à long terme.
"""

# Principes des tests unitaires

"""
Les tests unitaires consistent à écrire des fonctions de test qui vérifient que les fonctions et les méthodes d'un programme fonctionnent correctement. Les fonctions de test doivent vérifier le comportement des fonctions et des méthodes pour un ensemble de cas de test, en vérifiant que les résultats produits sont conformes aux attentes.

Voici un exemple de fonction de test pour une fonction "factorielle" qui calcule le factoriel d'un nombre entier :
"""

def test_factorielle():
    assert factorielle(0) == 1
    assert factorielle(1) == 1
    assert factorielle(5) == 120
    assert factorielle(10) == 3628800



"""
Dans cet exemple, la fonction de test "test_factorielle" vérifie que la fonction "factorielle" 
produit les résultats attendus pour un ensemble de cas de test.
 Chaque assertion vérifie le résultat produit par la fonction pour un cas de test particulier.
"""

# Utilisation de la bibliothèque unittest

"""
La bibliothèque unittest offre une API complète pour écrire et exécuter des tests unitaires en Python. 
On peut définir des classes de test, des cas de test et des méthodes de test, qui permettent de structurer les tests de manière élégante et efficace.

Voici un exemple de classe de test pour une fonction "factorielle" qui calcule le factoriel d'un nombre entier :
"""

import unittest

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

class TestFactorielle(unittest.TestCase):
    def test_factorielle_0(self):
        self.assertEqual(factorielle(0), 1)

    def test_factorielle_1(self):
        self.assertEqual(factorielle(1), 1)

    def test_factorielle_5(self):
        self.assertEqual(factorielle(5), 120)

    def test_factorielle_10(self):
        self
