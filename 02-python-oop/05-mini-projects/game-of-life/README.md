# Conway's Game of Life — Python (OOP)

Implémentation de l'automate cellulaire **Game of Life** de John Horton Conway, réalisée dans le cadre du mini-projet de la plateforme [365 Data Science](https://365datascience.com/), puis intégrée à mon portfolio Python.

---

## Objectif pédagogique

Ce projet a pour but de démontrer la maîtrise de la **Programmation Orientée Objet (POO)** en Python à travers un problème algorithmique classique. Il illustre :

- La création d'une **classe** avec son constructeur (`__init__`) et son état interne (la grille).
- L'encapsulation de la logique métier dans des **méthodes** dédiées (une par responsabilité).
- La manipulation de **structures de données** (listes 2D, voisinage, comptage).
- La **documentation** du code (docstrings, commentaires).

---

## Rappel des règles du Game of Life

Le Game of Life est un **jeu à zéro joueur** : une fois l'état initial posé, aucune intervention extérieure n'est nécessaire. La grille est finie (dimensions prédéfinies dans cette implémentation) et chaque cellule interagit avec ses **8 voisins** (horizontal, vertical, diagonal).

À chaque génération, les règles suivantes s'appliquent :

| État actuel de la cellule | Nombre de voisins vivants | État suivant |
| :--- | :--- | :--- |
| Vivante | 2 ou 3 | **Survit** |
| Vivante | 0 ou 1 | **Meurt** (solitude) |
| Vivante | 4 ou plus | **Meurt** (surpopulation) |
| Morte | exactement 3 | **Naît** |
| Morte | autre | **Reste morte** |

---

## Structure du projet

Le dossier `game-of-life/` contient deux fichiers :

- `game_of_life.py` — l'implémentation de la classe `GameOfLife`.
- `README.md` — ce fichier de documentation.

---

## Installation et exécution

### Prérequis

- **Python 3.8+**
- (Optionnel) `numpy` et `matplotlib` si vous utilisez la méthode de dessin graphique

### Cloner le dépôt

```bash
git clone https://github.com/younessov/python-projects.git

### Exécution

```bash
python3 game_of_life.py

## API de la classe `GameOfLife`

L'implémentation suit le squelette proposé par 365 Data Science. Voici les méthodes implémentées :

| Méthode | Rôle |
| :--- | :--- |
| `__init__(self, rows, cols)` | Initialise la grille avec les dimensions spécifiées (toutes cellules mortes). |
| `get_grid(self)` | Retourne la grille actuelle sous forme de liste 2D. |
| `print_grid(self)` | Affiche la grille dans le terminal (représentation lisible). |
| `populate(self, n)` | Place aléatoirement `n` cellules vivantes dans la grille. |
| `step(self)` | Calcule et applique une génération selon les règles du jeu. |
| `n_steps(self, n)` | Applique `n` générations successives. |
| `draw(self)` | (Optionnel) Affiche la grille graphiquement (Matplotlib). |

## Exemple d'utilisation

```python
from game_of_life import GameOfLife

# 1. Créer une grille 10x10
game = GameOfLife(rows=10, cols=10)

# 2. Peupler aléatoirement avec 20 cellules vivantes
game.populate(20)

# 3. Afficher l'état initial
game.print_grid()

# 4. Faire évoluer le jeu de 10 générations
game.n_steps(10)

# 5. Afficher l'état final
game.print_grid()

## Ce que j'ai appris

- **Modéliser un problème réel** (un automate cellulaire) sous forme de classe Python.
- **Séparer les responsabilités** : chaque méthode fait une seule chose (principe de responsabilité unique).
- **Gérer les cas limites** : bords de la grille, cellules sans voisins complets, etc.
- **Documenter** une classe et ses méthodes avec des docstrings au format PEP 257.

---

## Contexte du projet

Ce projet fait partie de mon portfolio global **[python-projects](https://github.com/younessov/python-projects)**, qui regroupe mes projets pédagogiques et professionnels en Python, Data Science, Machine Learning et Deep Learning.

- **Plateforme d'origine** : 365 Data Science
- **Section du portfolio** : `02-python-oop / 05-mini-projects`
- **Auteur** : Youness EDDAMEJ — Master Data Science

---

## Licence

Ce code est publié à des fins pédagogiques. Libre d'utilisation et de modification.
cd python-projects/02-python-oop/05-mini-projects/game-of-life
