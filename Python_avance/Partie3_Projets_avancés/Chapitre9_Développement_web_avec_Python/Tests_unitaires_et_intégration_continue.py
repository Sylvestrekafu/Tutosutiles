"""

Les tests unitaires et l'intégration continue sont des pratiques essentielles de la programmation moderne,
 qui permettent de garantir la qualité du code, d'assurer la conformité aux spécifications et d'optimiser
 la maintenance et l'évolution du code. Python offre une bibliothèque standard complète pour les tests unitaires,
 ainsi que des outils et des services pour l'intégration continue.

Dans ce chapitre, nous abordons les tests unitaires en Python, en montrant comment écrire des tests unitaires
pour des fonctions et des classes, en utilisant le module unittest de la bibliothèque standard.
Nous montrons également comment exécuter des tests unitaires et générer des rapports de test.

Nous abordons également l'intégration continue en Python, en montrant comment utiliser des outils
et des services tels que Travis CI, GitHub Actions et Jenkins pour exécuter des tests unitaires
de manière automatisée, et assurer une intégration continue du code.

Enfin, nous explorons les avantages des tests unitaires et de l'intégration continue en matière de qualité du code,
 de productivité et de réduction des coûts. Nous montrons comment les tests unitaires
  et l'intégration continue peuvent améliorer la qualité et la robustesse du code,
   réduire les coûts de maintenance et d'évolution du code, et augmenter la productivité des développeurs.
"""

# Tests unitaires

"""
Les tests unitaires sont une pratique courante de la programmation,
 qui consiste à tester des fonctions et des classes de manière isolée,
  en vérifiant que chaque fonction ou méthode fonctionne correctement dans toutes
   les conditions possibles. Python offre un module unittest de la bibliothèque standard,
    qui permet d'écrire et d'exécuter des tests unitaires de manière automatisée.

Voici un exemple de test unitaire pour une fonction de calcul de la moyenne :
"""

import unittest

def moyenne(liste):
    return sum(liste) / len(liste)

class TestMoyenne(unittest.TestCase):
    def test_moyenne_1(self):
        resultat = moyenne([1, 2, 3])
        self.assertEqual(resultat, 2)

    def test_moyenne_2(self):
        resultat = moyenne([])
        self.assertTrue(math.isnan(resultat))

    def test_moyenne_3(self):
        resultat = moyenne([1, "2", 3])
        self.assertRaises(TypeError)


"""
Dans cet exemple, on définit une fonction moyenne qui calcule la moyenne d'une liste,
 et on écrit trois tests unitaires pour cette fonction, en utilisant la classe TestCase du module unittest
 . Les tests vérifient que la fonction calcule correctement la moyenne, qu'elle gère correctement
  le cas d'une liste vide,
 et qu'elle lève une exception en cas de type de donnée incorrect.
"""

# Intégration continue

# L'intégration continue est une pratique courante de la programmation,
# qui consiste à exécuter des tests unitaires de manière automatisée à chaque modification du code source,
# afin de garantir la qualité et la stabilité du code, et d'éviter les régressions.
# Python offre de nombreux outils et services pour l'intégration continue, tels que Travis CI, GitHub Actions et Jenkins.
#
# Voici un exemple d'utilisation de Travis CI pour l'intégration continue d
