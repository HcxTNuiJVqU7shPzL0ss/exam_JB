"""Module for Lesson 02, Exam, grid.

Grid view.
This contains the Class which builds the board.
Regarding exam requirements, this file implements:
Version 1 - H
"""

#####################################################################
# Copyright 2026 gnoff
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#####################################################################


import random


# Access constants
from mypackage.constants import EMPTY, WALL, US_WALL, GAMER


class Grid:
    """Use to represent the board.

    It is possible to change the standard size, and signs for
    different squares.
    """

    empty = EMPTY               # Indicates an empty square
    wall = WALL                 # Indicates a wall
    unstable_wall = US_WALL     # Ind. a wall that may be breached
    gamer = GAMER               # Indicates the current gamer

    def __init__(self, player, width, height):
        """Use to create an object of the Class Grid.

        Initialize the attributes of a Grid object when the object
        is formed.
        Constructor (initializer) automatically called when
        creating a new instance of this class.
        """
        # The board is stored in a list of lists.
        # List comprehension is used to place the sign for
        # "empty" on each place on the board.
        self.width = width
        self.height = height
        self.data = [[self.empty for _ in range(self.width)]
                     for _ in range(self.height)]
        self.player = player


    def get(self, x, y):
        """Use to get what is on a certain position.

        Return the value at (x, y).
        Important:
        The grid is stored as a list of rows (data[row][column]).
        Therefore:
        y → row index
        x → column index
        This is why we access data[y][x] instead of data[x][y].
        """
        return self.data[y][x]

    def set(self, x, y, value):
        """Use to set what is on a certain position.

        Set the value at (x, y).
        The coordinate system uses (x, y), but the underlying
        structure is row-major (list of rows).
        So the correct indexing order is:
        data[y][x]
        Reversing this will cause out-of-range errors.
        """
        self.data[y][x] = value

    def set_player(self, player):
        """Use to handle player.

        Called from main (game), this method stores the
        attribute in player, same object as in main file.
        """
        self.player = player

    def clear(self, x, y):
        """Use to remove (clear) an item from a position."""
        self.set(x, y, self.empty)

    def __str__(self):
        """Use so the board can be displayed with print(grid)."""
        xs = ''
        for y, row in enumerate(self.data):
            for x, _ in enumerate(row):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += self.gamer
                else:
                    xs += str(row[x])
            xs += '\n'
        return xs


    def make_walls(self):
        """Use to create walls."""
        # First two are for walls around the board

        # Create the left and right border walls.
        # Loop over all rows (y = 0 → height-1)
        # and place a wall at:
        #   (0, y)               → left edge
        #   (width-1, y)         → right edge
        # Because the grid is stored as data[y][x],
        # 'i' represents the row index.
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        # Create the top and bottom border walls.
        # Loop over all columns (x = 1 → width-2)
        # and place a wall at:
        #   (x, 0)               → top edge
        #   (x, height-1)        → bottom edge
        # Here 'j' represents the column index.
        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)


        # Creates extra "inner" walls
        # Exam Version 1: H (Use for loops in grid.py to create more
        # than one connecting walls, though without creating a
        # room which you cannot enter.)
        for k in range(3, self.height // 2):
            # Create a vertical wall, starting at 3, moving to
            # maximum half the board
            self.set(10, k, self.unstable_wall)
            self.set(self.width - 1, k, self.wall)

        for m in range(13, self.width - 7):
            # Create a horizontal wall, starting at 13, moving
            # to leave 7 spaces after (including the actual
            # "fixed" wall to the right).
            self.set(m, 8, self.unstable_wall)
            self.set(m, self.height - 1, self.wall)


    # Used in the file pickups.py
    def get_random_x(self):
        """Use to randomize an x-pos on the board."""
        return random.randint(1, self.width - 1)

    def get_random_y(self):
        """Use to randomize a y-pos on the board."""
        return random.randint(1, self.height - 1)

    def is_empty(self, x, y):
        """Use to return True if nothing (empty) on the square."""
        return self.get(x, y) == self.empty
