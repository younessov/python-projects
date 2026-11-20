#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

class GameOfLife(object):  
    
    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        try:
            self.x_dim = int(x_dim)
            self.y_dim = int(y_dim)
            self.grid = [ [ 0 for j in range(y_dim) ] for i in range(x_dim) ]
        except ValueError:
            print("Invalid numeric value !")
        except TypeError:
            print("Dimensions must be an Integer !")
        except:
            print("Error During initialisation !")
    
    def get_grid(self):
        # Implement a getter method for your grid.
        return self.grid

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        for i in range (self.x_dim):
            for j in range ( self.y_dim ):
                print(f"{self.grid[i][j]} | ", end="")
            print()
            print("-" * (self.y_dim * 4 - 1))

    def populate_grid(self, coord):
        """
        Populates the game grid with live cells at the specified coordinates.
        Parameters:
        coord: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.
        Returns:
        The updated life_grid with the new live cells.
        """
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        for i,j in coord:
            self.grid[i][j]=1

    def make_step(self):
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        # Parcourir toutes les cellules
        new_grid = [ [ 0 for j in range(self.y_dim) ] for i in range(self.x_dim) ]
        
        for i in range (self.x_dim):
            for j in range ( self.y_dim ):
                s=0
                if (i==0):
                    if (j==0):
                        # ≄> (h,g) : pas de (haut-gauche)
                        s=self.grid[i+1][j] + self.grid[i+1][j+1] + self.grid[i][j+1]
                        
                    elif (j==self.y_dim-1):
                        # ≄> (h,d) : pas de (h,d)
                        s=self.grid[i+1][j] + self.grid[i+1][j-1] + self.grid[i][j-1]
                    else:
                        # ≄> (h) : pas de (h)
                        s=  self.grid[i+1][j] + self.grid[i+1][j-1] + self.grid[i+1][j+1] + self.grid[i][j-1] + self.grid[i][j+1]
                    
                elif (i==self.x_dim-1):
                    if (j==0):
                        # ≄> (b,g) : pas de (b,g)
                        s= self.grid[i-1][j] + self.grid[i][j+1] + self.grid[i-1][j+1]
                    elif (j==self.y_dim-1):
                        # ≄> (b,d) : pas de (b,d)
                        s= self.grid[i-1][j] + self.grid[i-1][j-1] + self.grid[i][j-1]
                    else:
                        # ≄> (b) : pas de (b)
                        s=self.grid[i-1][j] + self.grid[i-1][j-1] + self.grid[i-1][j+1] + self.grid[i][j-1] + self.grid[i][j+1]
                
                else:
                    if (j==0):
                        # ≄> (g) : pas de (g)
                        s= self.grid[i-1][j] + self.grid[i-1][j+1] + self.grid[i+1][j] + self.grid[i+1][j+1] + self.grid[i][j+1]
                    elif (j==self.y_dim-1):
                        # ≄> (d) : pas de (d)
                        s= self.grid[i-1][j] + self.grid[i-1][j-1] + self.grid[i+1][j] + self.grid[i+1][j-1] + self.grid[i][j-1]
                    else:
                        s = self.grid[i-1][j] + self.grid[i-1][j-1] + self.grid[i-1][j+1] + self.grid[i+1][j] + self.grid[i+1][j-1] + self.grid[i+1][j+1] + self.grid[i][j-1] + self.grid[i][j+1]
                if ( self.grid[i][j] == 1 ):
                    if ( s==0 or s==1 or s>=4):
                        new_grid[i][j] = 0
                    elif ( s==2 or s==3 ):
                        new_grid[i][j] = 1
                elif ( self.grid[i][j] == 0 ):
                    if ( s==3 ):
                        new_grid[i][j] = 1
        
        self.grid = new_grid

    def make_n_steps(self, n):
        # Implement a method that applies the make_step method n times.
        for _ in range(n):
            self.make_step()

    def draw_grid(self):
        fig, ax = plt.subplots()

        x_alive = []
        y_alive = []

        x_dead = []
        y_dead = []

        for i in range(self.x_dim):
            for j in range(self.y_dim):

                if self.grid[i][j] == 1:
                    x_alive.append(j)
                    y_alive.append(i)

                else:
                    x_dead.append(j)
                    y_dead.append(i)

        ax.scatter(x_alive, y_alive, color="black")
        ax.scatter(x_dead, y_dead, color="white")

        ax.set_xlim(-0.5, self.y_dim - 0.5)
        ax.set_ylim(self.x_dim - 0.5, -0.5)

        ax.set_xticks(np.arange(-0.5, self.y_dim, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, self.x_dim, 1), minor=True)

        ax.grid(which="minor", color="gray", linewidth=1)

        ax.set_aspect("equal")
        ax.tick_params(
            which="both",
            bottom=False,
            left=False,
            labelbottom=False,
            labelleft=False
        )

        plt.show()

# Création d'une grille de 10 lignes et 10 colonnes
game = GameOfLife(30, 30)

# Coordonnées initiales du Glider
'''
coord = [
    (0, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2)
]
'''
#coord = [(14, 15), (15, 15), (16, 15), (15, 14), (16, 16), (14, 16), (15, 17)]
#coord = [(10, 10), (10, 13), (11, 14), (12, 10), (12, 14), (13, 11), (13, 12), (13, 13), (13, 14)]
coord = [(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
(16, 14), (16, 15), (16, 17), (16, 18),
(18, 14), (18, 15), (18, 17), (18, 18),
(14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)]

# Population de la grille
game.populate_grid(coord)

# Affichage de la configuration initiale
c=0
while True:
    print("Génération initiale :")
    game.print_grid()
    game.draw_grid()
    game.make_step()
    c+=1
print("counter = ",c)
"""
# Population de la grille
game.populate_grid(coord)

# Affichage de la configuration initiale
print("Génération initiale :")
game.print_grid()
game.draw_grid()

# Calcul d'une génération
game.make_step()

print("Après une génération :")
game.print_grid()
game.draw_grid()

# Calcul de 4 générations supplémentaires
game.make_n_steps(4)

print("Après 5 générations :")
game.print_grid()
"""
game.draw_grid()
