# Conway's Game of Life — Python (OOP)

Implémentation de l'automate cellulaire **Game of Life** de John Horton Conway, réalisée dans le cadre d'un mini-projet de la plateforme [365 Data Science](https://365datascience.com/), puis intégrée à mon portfolio Python.

---

## Objectif pédagogique

Ce projet a pour objectif de mettre en pratique les concepts fondamentaux de la **programmation orientée objet (POO)** en Python à travers un problème algorithmique classique.

Il illustre notamment :

- La création d'une **classe** avec son constructeur (`__init__`) et son état interne (la grille).
- L'encapsulation de la logique métier dans des **méthodes** dédiées, chacune ayant une responsabilité précise.
- La manipulation de **structures de données** : listes bidimensionnelles, voisinage et comptage.
- La **documentation** du code à l'aide de docstrings et de commentaires.

---

## Rappel des règles du Game of Life

Le Game of Life est un **jeu à zéro joueur** (*zero-player game*) : une fois l'état initial défini, son évolution se déroule automatiquement, sans intervention extérieure.

La grille possède des dimensions prédéfinies dans cette implémentation. Chaque cellule interagit avec ses **8 voisines** : horizontales, verticales et diagonales.

À chaque génération, les règles suivantes s'appliquent :

| État actuel de la cellule | Nombre de voisins vivants | État suivant |
| :--- | :--- | :--- |
| Vivante | 2 ou 3 | **Survit** |
| Vivante | 0 ou 1 | **Meurt** (solitude) |
| Vivante | 4 ou plus | **Meurt** (surpopulation) |
| Morte | Exactement 3 | **Naît** |
| Morte | Autre nombre | **Reste morte** |

---

## Structure du projet

Le dossier `game-of-life/` contient les fichiers suivants :

- `game_of_life.py` — implémentation de la classe `GameOfLife`.
- `README.md` — documentation du projet.

---

## Installation et exécution

### Prérequis

- **Python 3.8+**
- (Optionnel) `numpy` et `matplotlib`, si vous utilisez les fonctionnalités de visualisation graphique.

### Cloner le dépôt

```bash
git clone https://github.com/younessov/python-projects.git
```

### Accéder au dossier du projet

```bash
cd python-projects/02-python-oop/05-mini-projects/game-of-life
```

### Exécuter le programme

```bash
python3 game_of_life.py
```

---

## API de la classe `GameOfLife`

L'implémentation s'appuie sur le squelette proposé par 365 Data Science.

Voici les principales méthodes implémentées :

| Méthode | Rôle |
| :--- | :--- |
| `__init__(self, rows, cols)` | Initialise la grille avec les dimensions spécifiées (toutes les cellules sont initialement mortes). |
| `get_grid(self)` | Retourne la grille actuelle sous forme de liste bidimensionnelle. |
| `print_grid(self)` | Affiche la grille dans le terminal sous une forme lisible. |
| `populate(self, n)` | Place aléatoirement `n` cellules vivantes dans la grille. |
| `step(self)` | Calcule et applique la génération suivante selon les règles du jeu. |
| `n_steps(self, n)` | Applique successivement `n` générations. |
| `draw(self)` | (Optionnel) Affiche graphiquement la grille à l'aide de Matplotlib. |

---

## Exemple d'utilisation

```python
from game_of_life import GameOfLife

# 1. Créer une grille de 10 x 10
game = GameOfLife(rows=10, cols=10)

# 2. Peupler aléatoirement la grille avec 20 cellules vivantes
game.populate(20)

# 3. Afficher l'état initial
game.print_grid()

# 4. Faire évoluer le jeu pendant 10 générations
game.n_steps(10)

# 5. Afficher l'état final
game.print_grid()
```

---

## Ce que j'ai appris

Ce projet m'a permis de mettre en pratique plusieurs notions importantes :

- **Modélisation** : représenter un problème algorithmique (automate cellulaire) à l'aide d'une classe Python.
- **Séparation des responsabilités** : organiser le code en méthodes indépendantes, chacune ayant un rôle précis.
- **Gestion des cas limites** : prendre en compte les bords de la grille et les cellules disposant de moins de huit voisines.
- **Documentation** : documenter une classe et ses méthodes à l'aide de docstrings conformes aux recommandations de la PEP 257.

---

## Contexte du projet

Ce projet fait partie de mon portfolio [**python-projects**](https://github.com/younessov/python-projects), qui regroupe mes projets pédagogiques et pratiques en Python, Data Science, Machine Learning et Deep Learning.

- **Plateforme d'origine** : 365 Data Science
- **Section du portfolio** : `02-python-oop / 05-mini-projects`
- **Auteur** : Youness EDDAMEJ — Master Data Science

---

## Licence

Ce code est publié à des fins pédagogiques. Il peut être librement utilisé et modifié.

